from transformers import pipeline

gen = pipeline(task="text2text-generation", model='google/flan-t5-base')

print('Please give one sentence in English:')
input_val = input().strip()

prompt = (
    "Paraphrase the input. Keep the meaning but change the wording; do not copy phrases. "
    "Return a single sentence with 8-24 words and end with a period.\n"
    f"Input: \"{input_val}\"\n"
)
# prompt = 'produce exactly ONE family-friendly joke. One sentence, 10-20 words, end with a period.'

print('\n--- TEXT GENERATION (FLAN-T5-base, deterministic) ---\n')

print(gen(
    prompt,
    max_new_tokens=48,
    num_beams=1,
    do_sample=True,
    top_p=0.9,
    temperature=0.9,
    no_repeat_ngram_size=3,
    repetition_penalty=1.2,
    length_penalty=1.0
)[0]['generated_text'])