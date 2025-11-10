#   Vocabulary

# - **Model**: a trained neural network that maps input text to output text or labels.
# - **Weights / checkpoint**: the learned parameters of that model (the big files we download).
# - **Tokenizer**: converts text → **tokens** (subwords/IDs) for the model, and back again.
# - **Tokens**: pieces of text (not necessarily full words). Length limits and speeds are
#   measured in tokens, so “max_new_tokens” is about subwords, not words.
# - **Transformer (architecture)**: the neural network design (self-attention, etc.) used
#   by most state-of-the-art language models.
# - **Transformers (library)**: the Hugging Face Python library we import to use models.
# - **Pipeline**: a prebuilt function (e.g., `pipeline("sentiment-analysis")`) that handles
#   tokenizer + model + decoding for a common task.
# - **Inference** vs **training**:
#   * Inference = using a trained model to make predictions.
#   * Training/fine-tuning = updating weights with data.
# - **Encoder–decoder** vs **decoder-only**:
#   * Encoder–decoder (e.g., T5/BART): good for text-to-text tasks (summarize/translate).
#   * Decoder-only (e.g., GPT-style): good for next-token text continuation.
# - **Deterministic decoding** (beam search, no sampling): stable, repeatable outputs.
# - **Sampling** (temperature, top-p): more creative/varied but less predictable.



# vocabulary sheet 

# ————— Core concepts —————
# - **Model**: a trained neural network that maps input text to output text/labels.
# - **Weights / checkpoint**: the large files with the model’s learned parameters.
# - **Inference** vs **training**: using a model to predict vs. updating its weights with data.

# ————— Tokenization —————
# - **Tokenizer**: converts text ↔ tokens (integers). Loaded with `AutoTokenizer`.
# - **Token / Token ID**: a subword unit represented as an integer (what the model actually reads).
# - **Vocabulary**: the set of all tokens a tokenizer knows.
# - **WordPiece**: tokenizer family used by BERT/DistilBERT (often uncased; adds special tokens).
# - **SentencePiece**: tokenizer family used by T5/FLAN & Marian/OPUS-MT (language-agnostic subwords).
# - **Detokenize**: convert token IDs back into human-readable text (optionally hiding special tokens).

# ————— Special tokens you’ll see —————
# - **[CLS]**: “classification” token at the start for BERT-style models (pooled summary for classifiers).
# - **[SEP]**: “separator/end” token at the end (and between paired sentences) for BERT-style models.
# - **</s> (EOS)**: end-of-sequence token used by T5/FLAN to signal “stop generating”.
# - **<pad>**: padding token used to equalize sequence lengths inside a batch.
# - **Pad token id**: the integer ID representing `<pad>` (e.g., 0 for many T5/FLAN models).

# ————— Tensors & shapes —————
# - **Shape [B, L]**: tensors print as `torch.Size([batch_size, sequence_length])`.
# - **Batch size (B)**: how many sequences we process at once.
# - **Sequence length (L)**: number of **tokens** after tokenization (not characters/words).
# - **attention_mask**: `[B, L]` tensor with 1=real token, 0=padding; tells the model to ignore pads.
# - **Padding**: add `<pad>` tokens so all sequences in a batch share the same length.
# - **Truncation**: cut inputs longer than a chosen `max_length` (protects CPU time/memory).

# ————— Pipelines & Auto classes —————
# - **Pipeline**: a prebuilt function (e.g., `pipeline("summarization")`) bundling tokenizer+model+decoding.
# - **Auto classes**: factory loaders that pick correct components, e.g.:
#   `AutoTokenizer.from_pretrained("google/flan-t5-base")`,
#   `AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")`.

# ————— Model families we use —————
# - **FLAN-T5 (encoder–decoder / seq2seq)**: instruction-tuned T5 (great for text-to-text tasks).
# - **DistilBERT (encoder-only)**: lightweight BERT for classification (expects [CLS]…[SEP]).
# - **DistilBART-CNN (encoder–decoder)**: distilled BART fine-tuned for news summarization.
# - **OPUS-MT / Marian (encoder–decoder)**: translation models (e.g., EN→SV), SentencePiece-based.
# - **Distillation**: compressing a large “teacher” into a smaller, faster “student” model.

# ————— Generation (decoding) —————
# - **`.generate(...)`**: turns input token IDs into new output token IDs.
# - **Greedy**: always pick the top next token (deterministic, safe).
# - **Beam search (`num_beams`)**: explore several high-probability paths; often more fluent; can repeat.
# - **Sampling (`do_sample=True`)**: add randomness; tune with **temperature** and **top_p** for creativity.
# - **`max_new_tokens`**: cap on how many **generated** tokens to produce.
# - **`no_repeat_ngram_size`**: discourages repeating short phrases (reduces loops/copypasta).
# - **`length_penalty`**: bias beams toward shorter/longer outputs.
# - **`skip_special_tokens=True`**: hide special tokens when decoding to text.

# ————— Performance & timing —————
# - **`time.perf_counter()`**: high-resolution wall-clock timer for quick benchmarks.
# - **Latency vs throughput**: time per call vs items per second (batching improves throughput).
# - **Warm-up / caches**: first call is slower; later calls are faster (weights loaded, kernels warmed).
# - **Scaling with L²**: attention cost grows roughly with the square of sequence length—keep prompts short on CPU.
 
 
 
 
 


# "How a pipeline call works (mental model):"
#   1) Your input text → **tokenizer** → token IDs.
#   2) Token IDs → **model** (forward pass on CPU) → output logits.
#   3) **Decoding** turns logits into text (beam search or sampling).
#   4) Output tokens → detokenize → final string.


#   Setup
#   text-to-text generation
#   sentiment analysis
#   Summarization
#   Translation


#   transformers
#   accelerate

# Windows: C:\Users\<you>\.cache\huggingface




# -----------------------------------------------------------------------------
# Part 1- Text Generation with FLAN-T5-base
# -----------------------------------------------------------------------------


from transformers import pipeline

gen = pipeline("text2text-generation", model="google/flan-t5-base")

prompt = (
    "Produce exactly ONE family-friendly joke. "
    "One sentence, 10-20 words, end with a period."
)

print("\n--- TEXT GENERATION (FLAN-T5-base, deterministic) ---\n")

print(gen(
    prompt,
    max_new_tokens=32,
    num_beams=5,
    no_repeat_ngram_size=3,
    do_sample=False
)[0]["generated_text"])

# -----------------------------------------------------------------------------
# Part 2- Sentiment Analysis (DistilBert model)
# -----------------------------------------------------------------------------

sentiment = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

print("\n--- SENTIMENT ANALYSIS ---\n")

examples = [
    "I absolutely love coding in Python!",
    "This bug is driving me crazy.",
    "It's okay, not great, not terrieble."
]
for text in examples:
    result = sentiment(text)[0]
    print(f"Text: {text}\n→ Label: {result['label']}, Score: {result['score']:.3f}\n")

# -----------------------------------------------------------------------------
# Part 3- Summarization (DistilBART CNN)
# -----------------------------------------------------------------------------

from transformers import pipeline


summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

print("\n--- SUMMARIZATION ---\n")


article = (
    "Python is a popular programming language known for readability and a rich ecosystem. "
    "Hugging Face Transformers lets developers run state-of-the-art AI models locally. "
    "With pipelines, tasks like text generation, sentiment analysis, and summarization "
    "become easy to prototype."    
)

summary = summarizer(
    article, 
    max_length = 20,    #subword pieces...NOT words
    min_length=15,
    do_sample = False
    )[0]["summary_text"]

print("Orginal:", article)
print("\nSummary:", summary)

# -----------------------------------------------------------------------------
# Part 4- Translation (En-> SV) (OPUS-MT)
# -----------------------------------------------------------------------------

print("\n--- TRANSLATION (EN→SV) ---\n")


from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-sv")

english = "Transformers pipelines make it simple to try models locally."
swedish = translator(english)[0]["translation_text"]

print("EN:", english)
print("SV:", swedish)



# vocabulary sheet 

# ————— Core concepts —————
# - **Model**: a trained neural network that maps input text to output text/labels.
# - **Weights / checkpoint**: the large files with the model’s learned parameters.
# - **Inference** vs **training**: using a model to predict vs. updating its weights with data.

# ————— Tokenization —————
# - **Tokenizer**: converts text ↔ tokens (integers). Loaded with `AutoTokenizer`.
# - **Token / Token ID**: a subword unit represented as an integer (what the model actually reads).
# - **Vocabulary**: the set of all tokens a tokenizer knows.
# - **WordPiece**: tokenizer family used by BERT/DistilBERT (often uncased; adds special tokens).
# - **SentencePiece**: tokenizer family used by T5/FLAN & Marian/OPUS-MT (language-agnostic subwords).
# - **Detokenize**: convert token IDs back into human-readable text (optionally hiding special tokens).

# ————— Special tokens you’ll see —————
# - **[CLS]**: “classification” token at the start for BERT-style models (pooled summary for classifiers).
# - **[SEP]**: “separator/end” token at the end (and between paired sentences) for BERT-style models.
# - **</s> (EOS)**: end-of-sequence token used by T5/FLAN to signal “stop generating”.
# - **<pad>**: padding token used to equalize sequence lengths inside a batch.
# - **Pad token id**: the integer ID representing `<pad>` (e.g., 0 for many T5/FLAN models).

# ————— Tensors & shapes —————
# - **Shape [B, L]**: tensors print as `torch.Size([batch_size, sequence_length])`.
# - **Batch size (B)**: how many sequences we process at once.
# - **Sequence length (L)**: number of **tokens** after tokenization (not characters/words).
# - **attention_mask**: `[B, L]` tensor with 1=real token, 0=padding; tells the model to ignore pads.
# - **Padding**: add `<pad>` tokens so all sequences in a batch share the same length.
# - **Truncation**: cut inputs longer than a chosen `max_length` (protects CPU time/memory).

# ————— Pipelines & Auto classes —————
# - **Pipeline**: a prebuilt function (e.g., `pipeline("summarization")`) bundling tokenizer+model+decoding.
# - **Auto classes**: factory loaders that pick correct components, e.g.:
#   `AutoTokenizer.from_pretrained("google/flan-t5-base")`,
#   `AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")`.

# ————— Model families we use —————
# - **FLAN-T5 (encoder–decoder / seq2seq)**: instruction-tuned T5 (great for text-to-text tasks).
# - **DistilBERT (encoder-only)**: lightweight BERT for classification (expects [CLS]…[SEP]).
# - **DistilBART-CNN (encoder–decoder)**: distilled BART fine-tuned for news summarization.
# - **OPUS-MT / Marian (encoder–decoder)**: translation models (e.g., EN→SV), SentencePiece-based.
# - **Distillation**: compressing a large “teacher” into a smaller, faster “student” model.

# ————— Generation (decoding) —————
# - **`.generate(...)`**: turns input token IDs into new output token IDs.
# - **Greedy**: always pick the top next token (deterministic, safe).
# - **Beam search (`num_beams`)**: explore several high-probability paths; often more fluent; can repeat.
# - **Sampling (`do_sample=True`)**: add randomness; tune with **temperature** and **top_p** for creativity.
# - **`max_new_tokens`**: cap on how many **generated** tokens to produce.
# - **`no_repeat_ngram_size`**: discourages repeating short phrases (reduces loops/copypasta).
# - **`length_penalty`**: bias beams toward shorter/longer outputs.
# - **`skip_special_tokens=True`**: hide special tokens when decoding to text.

# ————— Performance & timing —————
# - **`time.perf_counter()`**: high-resolution wall-clock timer for quick benchmarks.
# - **Latency vs throughput**: time per call vs items per second (batching improves throughput).
# - **Warm-up / caches**: first call is slower; later calls are faster (weights loaded, kernels warmed).
# - **Scaling with L²**: attention cost grows roughly with the square of sequence length—keep prompts short on CPU.



# -----------------------------------------------------------------------------
# Part 5- Token & Tokenizer
# -----------------------------------------------------------------------------

#   • FLAN-T5-base → SentencePiece tokenizer (encoder–decoder model).
#   • DistilBERT   → WordPiece tokenizer (encoder-only classifier, uncased)."


from transformers import AutoTokenizer

text = "Transformers make local demos easy. Python is great for teaching."

#   FLAN-T5-base tokenizer (SentencePiece):

tok_flan = AutoTokenizer.from_pretrained("google/flan-t5-base")

ids_flan = tok_flan.encode(text)


print("\n--- TOKENS: Flan-T5 (SentencePiece) ---")

print("Token IDs:", ids_flan[:20], "...")   #1 (last ID)

print("Decoded:", tok_flan.decode(ids_flan)) #`</s>` (EOS marker)


# DistilBERT (WordPiece tokenizer)

tok_bert = AutoTokenizer.from_pretrained("distilbert-base-uncased")  #[CLS]=101 [SEP]=102

ids_bert = tok_bert.encode(text)

print("\n--- TOKENS: DistilBERT (WordPiece) ---")

print("Token IDs:", ids_bert[:20], "...")

print("Decoded:", tok_bert.decode(ids_bert))


# -----------------------------------------------------------------------------
# Part 6- From pipeline to Auto classes
# -----------------------------------------------------------------------------


import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM  


device = torch.device("cpu")

model_id = "google/flan-t5-base"

tok = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForSeq2SeqLM.from_pretrained(model_id).to(device)

prompt = (
    "Rewrite the sentence in simpler English. Output one sentence, end with a period.\n"
    "Sentence: 'Transformers lets us try modern AI models locally for teaching.'\n"
    "Output:"   
)

# Encode

enc = tok(prompt, return_tensors = "pt").to(device)

# "Tokenize to PyTorch tensors. We get:
#    • input_ids: the integer tokens the model will read,
#    • attention_mask: 1 for real tokens, 0 for padding.


print("\n--- SHAPES (inputs) ---")  # [batch_size, sequence_length]
print("input_ids: ", enc.input_ids.shape) # torch.Size([B, L])
print("attention_mask: ", enc.attention_mask.shape) # torch.Size([B, L])

# "Why do we care about L? Because Transformer compute/memory scales roughly with L²
#  (self-attention compares each token to every other).

# Generate:

with torch.no_grad():
    out_ids = model.generate(
        **enc,
        max_new_tokens = 32,
        num_beams = 5,
        no_repeat_ngram_size = 3,
        do_sample=False
    )

print("\n--- SHAPES (outputs) ---")
print("out_ids:", out_ids.shape) # torch.Size([B, L])


# Decode

out_text = tok.decode(out_ids[0], skip_special_tokens = True) # skip special token ex. </s>.

print("\n--- MANUAL GENERATION (FLAN-T5) ---\n")
print(out_text)


# Sum:

# tokenize → generate → decode.
# [batch, seq_len]