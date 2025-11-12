import pandas as pd
import json

df = pd.read_csv('data/indian_food.csv')
recipes = []

for i, row in df.iterrows():
    if pd.isna(row['ingredients']):
        continue
    recipes.append({
        "id": f"r{i}",
        "title": row['name'],
        "ingredients": [x.strip().lower() for x in row['ingredients'].split(',')],
        "diet": row.get('diet', 'unknown'),
        "cook_time": int(row.get('prep_time', 0)) if not pd.isna(row.get('prep_time')) else 0,
        "tags": [row.get('diet','')]
    })

with open('data/recipes.json', 'w', encoding='utf-8') as f:
    json.dump(recipes, f, indent=2, ensure_ascii=False)

print("✅ Saved to data/recipes.json")
