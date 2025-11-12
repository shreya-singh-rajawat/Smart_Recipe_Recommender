import os
import requests
from dotenv import load_dotenv

load_dotenv()

SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

def get_recipes_from_spoonacular(ingredients, number=5):
    """
    Fetches recipe recommendations from the Spoonacular API
    based on provided ingredients.
    """
    if not SPOONACULAR_API_KEY:
        return {"error": "Missing Spoonacular API key"}

    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ",".join(ingredients),
        "number": number,
        "apiKey": SPOONACULAR_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Simplify output
        recipes = [
            {
                "title": item["title"],
                "image": item["image"],
                "usedIngredientCount": item["usedIngredientCount"],
                "missedIngredientCount": item["missedIngredientCount"],
                "id": item["id"]
            }
            for item in data
        ]
        return recipes

    except Exception as e:
        print("Spoonacular API error:", e)
        return {"error": str(e)}
