import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open('data/recipes.json', 'r', encoding='utf-8') as f:
    recipes = json.load(f)

# Convert ingredients to text
texts = [" ".join(r['ingredients']) for r in recipes]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

def recommend_recipes(user_ingredients, top_n=5):
    user_text = " ".join(user_ingredients)
    user_vec = vectorizer.transform([user_text])
    sim_scores = cosine_similarity(user_vec, tfidf_matrix)[0]
    top_indices = sim_scores.argsort()[-top_n:][::-1]
    results = [
        {
            "title": recipes[i]['title'],
            "score": round(sim_scores[i], 3),
            "ingredients": recipes[i]['ingredients'],
            "cook_time": recipes[i].get("cook_time", "N/A")  # Use "N/A" if missing
        }
        for i in top_indices
    ]
    return results

def generate_grocery_list(recipes):
    """
    recipes: list of recipe dicts (as returned from recommend function)
    returns: sorted unique grocery items list
    """
    items = []
    for r in recipes:
        items.extend([ing.strip().lower() for ing in r.get("ingredients", [])])
    unique = sorted(set(items))
    return unique

