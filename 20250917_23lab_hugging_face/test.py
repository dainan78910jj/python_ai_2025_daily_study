import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, infer_device

device = infer_device()

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
inputs = tokenizer("Hugging Face is an open-source company", return_tensors="pt").to(device)

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base", dtype=torch.float16).to(device)


# explicitly set to 100 because Llama2 generation length is 4096
outputs = model.generate(**inputs, max_new_tokens=50, do_sample=True, num_beams=1)
tokenizer.batch_decode(outputs, skip_special_tokens=True)

print(outputs) 