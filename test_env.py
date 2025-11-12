from transformers import pipeline

# Create a local text-generation pipeline using GPT-2
generator = pipeline("text-generation", model="gpt2")

# Prompt
prompt = "Create a 7-day healthy Indian-style meal plan using potato, rice, and tomato."

# Generate text
result = generator(prompt, max_new_tokens=150, do_sample=True, temperature=0.7)

# Print output
print(result[0]["generated_text"])
from transformers import pipeline

# Create a local text-generation pipeline using GPT-2
generator = pipeline("text-generation", model="gpt2")

# Prompt
prompt = "Create a 7-day healthy Indian-style meal plan using potato, rice, and tomato."

# Generate text
result = generator(prompt, max_new_tokens=150, do_sample=True, temperature=0.7)

# Print output
print(result[0]["generated_text"])
