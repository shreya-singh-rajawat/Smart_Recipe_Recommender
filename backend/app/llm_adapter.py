# backend/app/llm_adapter.py
from transformers import pipeline

try:
    generator = pipeline("text-generation", model="gpt2")
    LLM_AVAILABLE = True
except Exception as e:
    print(f"[LLM] Failed to load local model: {e}")
    generator = None
    LLM_AVAILABLE = False


def generate_meal_plan(ingredients, days=7):
    """
    Generates a meal plan using local GPT-2 model.
    """
    if not LLM_AVAILABLE:
        return f"[LLM not available] Could not generate meal plan. Ingredients: {', '.join(ingredients)}"

    prompt = (
        f"Create a detailed {7}-day healthy Indian-style meal plan using these ingredients: "
        f"{', '.join(ingredients)}. Include breakfast, lunch, and dinner for each day, "
        "and describe briefly how each dish is prepared."
    )

    print(f"[LLM] Prompt: {prompt}\n")

    result = generator(prompt, max_new_tokens=250, do_sample=True, temperature=0.8)
    text = result[0]["generated_text"]

    return text
