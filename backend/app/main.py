# backend/app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os, requests

from .api_adapter import get_recipes_from_spoonacular
from .recommender import recommend_recipes, generate_grocery_list
from .llm_adapter import generate_meal_plan, LLM_AVAILABLE

# Load environment variables
load_dotenv()

SPOONACULAR_KEY = os.getenv("SPOONACULAR_API_KEY")

app = FastAPI(title="Smart Recipe Recommender")


# -----------------------------
# ✅ Pydantic Models
# -----------------------------
class RecipeRequest(BaseModel):
    ingredients: list
    diet: str | None = None
    max_time: int | None = None
    top_n: int | None = 5


# -----------------------------
# ✅ API Endpoints
# -----------------------------

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart Recipe Recommender API!"}


# POST /recommend
@app.post("/recommend")
def recommend(request: RecipeRequest):
    results = recommend_recipes(request.ingredients)
    return {"results": results}


# POST /mealplan
@app.post("/mealplan")
def mealplan(request: RecipeRequest):
    plan = generate_meal_plan(request.ingredients, days=3)
    return {"meal_plan": plan, "llm_available": LLM_AVAILABLE}


# POST /grocerylist
@app.post("/grocerylist")
def grocerylist(request: RecipeRequest):
    recs = recommend_recipes(request.ingredients)
    groceries = generate_grocery_list(recs)
    return {"grocery_list": groceries, "recipes_count": len(recs)}


# GET /spoonacular_search?q=...
@app.get("/spoonacular_search")
def spoonacular_search(q: str, number: int = 5):
    if not SPOONACULAR_KEY:
        return {"error": "SPOONACULAR_API_KEY not set in .env"}

    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {"query": q, "number": number, "apiKey": SPOONACULAR_KEY}

    resp = requests.get(url, params=params, timeout=10)
    if resp.status_code != 200:
        return {
            "error": "Spoonacular API error",
            "status_code": resp.status_code,
            "details": resp.text,
        }
    return resp.json()


# POST /recipes
@app.post("/recipes")
def get_recipes(request: RecipeRequest):
    """Fetch recipes directly from Spoonacular API"""
    return get_recipes_from_spoonacular(request.ingredients)


# -----------------------------
# ✅ Local Run Entry Point
# -----------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)
