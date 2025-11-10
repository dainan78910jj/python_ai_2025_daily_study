# %% [markdown]
# Todays Lab 2025-09-22
#  
# Implement a small script that (1) batches inputs with padding/truncation, (2) generates outputs with three decoding strategies (greedy, beam, sampling), (3) runs simple automatic checks on the outputs, and (4) times single vs. small-batch runs — all locally on CPU.
#  
# Use this model & setup:
#  
# - Model: google/flan-t5-base
#  
# - Run on CPU only.
#  
# - Tokenization must use padding=True, truncation=True, and your chosen max_length (justify by comment in code).
#  
# - For generation use the same max_new_tokens across all strategies so results are comparable.
#  
#  
# Fixed prompt set (use these exact 12 prompts)
#  
# Rewrite (4)
# 1) Rewrite the sentence in simpler English. End with a period. Sentence: 'Python’s clear syntax helps beginners focus on problem-solving.' Output:
# 2) Rewrite the sentence in simpler English. End with a period. Sentence: 'Version control lets teams track changes and work safely together.' Output:
# 3) Rewrite the sentence in simpler English. End with a period. Sentence: 'Preprocessing text often includes lowercasing and removing extra spaces.' Output:
# 4) Rewrite the sentence in simpler English. End with a period. Sentence: 'Short prompts run faster on CPU because attention scales with length.' Output:
#  
# Explain (4)
# 5) Explain in one sentence what a learning rate does. End with a period.
# 6) Explain in one sentence what an API key is used for. End with a period.
# 7) Explain in one sentence what a unit test checks. End with a period.
# 8) Explain in one sentence what a tokenizer does in NLP. End with a period.
#  
# Summarize (4)
# 9) Summarize in one sentence: 'Pipelines bundle tokenization, the model, and decoding. They are great for quick demos on CPU.' Output:
# 10) Summarize in one sentence: 'Batching several prompts can improve throughput. Padding and masks keep shapes compatible.' Output:
# 11) Summarize in one sentence: 'Beam search is deterministic and often fluent. Sampling adds creativity but may drift.' Output:
# 12) Summarize in one sentence: 'SentencePiece and WordPiece split text into subwords. This keeps vocabulary small and improves coverage.' Output:
#  
#  
# A) Batch tokenization (padding & truncation)
#  
# - Batch all 12 prompts (you may prepend a short instruction like Respond in one sentence: if you want).
#  
# - Tokenize with padding=True, truncation=True, and max_length you choose (briefly comment in code why).
#  
# - Print:
# input_ids.shape and attention_mask.shape
# The tokenizer’s pad token id
# (Optional) Print the last row of attention_mask to show 1s (real tokens) vs 0s (padding).
#  
#  
# B) Decode the same batch three ways
# Run generation for the exact same tokenized batch with these strategies and print outputs for each prompt:
#  
# - Greedy: do_sample=False, num_beams=1
#  
# - Beam: do_sample=False, num_beams = 3 or 5 (pick one and note it in a comment)
#  
# - Sampling: do_sample=True with your chosen temperature (≈0.7–0.9) and top_p (≈0.8–0.95)
#  
# For each prompt, print three one-liners labeled [Greedy], [Beam], [Sample]. Keep them on separate lines or in a simple table.
#  
# C) Automatic checks (programmatic, no prose)
# Write functions to check each generated line (no manual judging):
#  
# 1. One sentence? (exactly one terminal punctuation among . ! ?)
#  
# 2. Ends with a period?
#  
# 3. Word count window (choose a window, e.g., 8–24 words)
#  
# 4. Repetition flag (detect repeated bigrams/trigrams or obvious loops)
#  
# Compute, per strategy (Greedy/Beam/Sampling):
#  
# - Constraint pass-rate = % that pass checks 1+2+3
#  
# - Avg. word count (and optionally std dev)
#  
# - % with repetition (from check 4)
#  
# Print a compact summary table to the console (one row per strategy).
#  
# (Optional) Add a simple on-topic keyword flag per prompt if you want; otherwise skip.
#  
#  
# D) Tiny timing
# Measure on CPU with time.perf_counter():
# - Single input: tokenize → generate for 1 representative prompt (use the same max_new_tokens).
# - Small batch: tokenize → generate for a batch (use all 12 prompts, or duplicate them once).
#  
# Print two numbers (seconds, 3 decimals):
# Single input: ~Xs
# Small batch : ~Ys
#  

# %%


rewrite_sentences = [
    'Python’s clear syntax helps beginners focus on problem-solving.',
    'Version control lets teams track changes and work safely together.',
    'Preprocessing text often includes lowercasing and removing extra spaces.',
    'Short prompts run faster on CPU because attention scales with length.'   
]

explain_sentences = [
    'what a learning rate does. End with a period.',
    'what an API key is used for. End with a period.',
    'what a unit test checks. End with a period.',
    'what a tokenizer does in NLP. End with a period.'
]

summarize_sentences = [
    'Pipelines bundle tokenization, the model, and decoding. They are great for quick demos on CPU.',
    'Batching several prompts can improve throughput. Padding and masks keep shapes compatible.',
    'Beam search is deterministic and often fluent. Sampling adds creativity but may drift.',
    'SentencePiece and WordPiece split text into subwords. This keeps vocabulary small and improves coverage.'
]

full_prompts = (
    [f"Rewrite the sentence in simpler English. End with a period. Sentence: {s}" for s in rewrite_sentences] +
    [f"Explain in one sentence: {s}" for s in explain_sentences] +
    [f"Summarize in one sentence: {s}" for s in summarize_sentences]
)

 
# Print a compact summary table to the console (one row per strategy).
def check(inputs):
    import re
    from collections import Counter
    
    strategies = ['Greedy', 'Beam', 'Sample']
    results = {}
    
    for i, strategy in enumerate(strategies):
        outputs = inputs[i]
        total = len(outputs)
        
        # Counters for checks
        one_sentence_count = 0
        ends_with_period_count = 0
        word_count_window_count = 0
        repetition_count = 0
        
        word_counts = []
        
        for output in outputs:
            # Check 1: One sentence? (exactly one terminal punctuation among . ! ?)
            terminal_punctuation = len(re.findall(r'[.!?]', output))
            if terminal_punctuation == 1:
                one_sentence_count += 1
            
            # Check 2: Ends with a period?
            if output.strip().endswith('.'):
                ends_with_period_count += 1
            
            # Check 3: Word count window (choose a window, e.g., 8–24 words)
            words = output.strip().split()
            word_count = len(words)
            word_counts.append(word_count)
            if 8 <= word_count <= 24:
                word_count_window_count += 1
            
            # Check 4: Repetition flag (detect repeated bigrams/trigrams or obvious loops)
            has_repetition = False
            words = [w.strip('.,!?;') for w in words]  # Clean words for repetition check
            
            # Check for repeated bigrams
            if len(words) >= 4:  # Need at least 4 words to have 2 bigrams
                bigrams = [tuple(words[j:j+2]) for j in range(len(words)-1)]
                bigram_counts = Counter(bigrams)
                if any(count > 1 for count in bigram_counts.values()):
                    has_repetition = True
            
            # Check for repeated trigrams if not already flagged
            if not has_repetition and len(words) >= 6:  # Need at least 6 words to have 2 trigrams
                trigrams = [tuple(words[j:j+3]) for j in range(len(words)-2)]
                trigram_counts = Counter(trigrams)
                if any(count > 1 for count in trigram_counts.values()):
                    has_repetition = True
            
            if has_repetition:
                repetition_count += 1
        
        # Compute metrics
        constraint_pass_rate = ((one_sentence_count + ends_with_period_count + word_count_window_count) / (3 * total)) * 100
        avg_word_count = sum(word_counts) / len(word_counts) if word_counts else 0
        repetition_percentage = (repetition_count / total) * 100
        
        results[strategy] = {
            'constraint_pass_rate': constraint_pass_rate,
            'avg_word_count': avg_word_count,
            'repetition_percentage': repetition_percentage
        }
    
    # Print a compact summary table to the console (one row per strategy)
    print(f"{'Strategy':<10} {'Pass Rate (%)':<15} {'Avg Words':<12} {'Repetition (%)':<15}")
    print("-" * 55)
    for strategy in strategies:
        pass_rate = results[strategy]['constraint_pass_rate']
        avg_words = results[strategy]['avg_word_count']
        repetition = results[strategy]['repetition_percentage']
        print(f"{strategy:<10} {pass_rate:<15.2f} {avg_words:<12.2f} {repetition:<15.2f}")
    
    return results

# %%
import time
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
device = torch.device("cpu")

t0 = time.perf_counter()

token_output = tokenizer(
    full_prompts,
    return_tensors="pt", 
    padding=True, 
    truncation=True, 
    max_length=96  # Chosen to accommodate longer prompts while being efficient on CPU
).to(device)

#Greedy decoding
g = model.generate(
    **token_output,
    max_new_tokens=64,
    do_sample=False,
    num_beams=1 
)

#Beam search
b = model.generate(
    **token_output,
    max_new_tokens = 64,
    do_sample = False,
    num_beams=5 # Using 5 as suggested in the comments
)

# Sampling
s = model.generate(
    **token_output,
    max_new_tokens = 64,
    do_sample = True,
    temperature=0.8,  # Mid-range temperature for balanced creativity
    top_p=0.9, 
    num_return_sequences = 1
)

t1 = time.perf_counter()

res = (
    tokenizer.batch_decode(g, skip_special_tokens=True), 
    tokenizer.batch_decode(b, skip_special_tokens=True),
    tokenizer.batch_decode(s, skip_special_tokens=True),
)

t2 = time.perf_counter()

print(f"Single input: ~{(t1-t0):.3f}s")
print(f"Small batch: ~{(t2-t1):.3f}s")

print("input_ids shape:", token_output.input_ids.shape) #[B, L]
print("attention_mask shape:", token_output.attention_mask.shape)
print("Pad token id :", tokenizer.pad_token_id)
print("\nGenerated outputs:")
print("="*50)

# Print outputs for each prompt with the three strategies
for i, prompt in enumerate(full_prompts):
    print(f"\nPrompt {i+1}: {prompt}")
    print(f"[Greedy]  : {res[0][i]}")
    print(f"[Beam]    : {res[1][i]}")
    print(f"[Sample]  : {res[2][i]}")

print("\n\nCheck results:")
print("="*50)

check_res = check(res)
