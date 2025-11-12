# frontend/app.py
import streamlit as st
import requests, os
import pandas as pd
import plotly.express as px

API = os.getenv("API_BASE", "http://127.0.0.1:8000")

st.set_page_config(layout="wide", page_title="Smart Recipe Recommender")
st.title("🍳 Smart Recipe Recommender")

with st.sidebar:
    st.header("Search")
    ingredients_text = st.text_area("Ingredients (comma separated)", height=120)
    diet = st.selectbox("Diet", options=["", "vegan", "vegetarian", "non-vegetarian","keto"])
    max_time = st.slider("Max cook time (min)", 0, 100, 45,50)
    top_n = st.number_input("Results", min_value=1, max_value=10, value=5)

    if st.button("Find Recipes"):
        ing_list = [x.strip().lower() for x in ingredients_text.split(",") if x.strip()]
        payload = {"ingredients": ing_list, "diet": diet or None, "max_time": max_time, "top_n": top_n}

        try:
            res = requests.post(f"{API}/recommend", json=payload, timeout=15)
            data = res.json()

            # ✅ Handle both dict and list responses safely
            if isinstance(data, list):
                st.session_state["results"] = data
            elif isinstance(data, dict):
                st.session_state["results"] = data.get("results", [])
            else:
                st.session_state["results"] = []

            st.session_state["ing_list"] = ing_list

        except Exception as e:
            st.error(f"API error: {e}")
            st.session_state["results"] = []

# show results
if "results" in st.session_state and st.session_state["results"]:
    st.subheader("Recommended Recipes")
    cols = st.columns(2)

    for i, r in enumerate(st.session_state["results"]):
        with cols[i % 2]:
            st.markdown(f"### {r.get('title', 'Untitled Recipe')}")
            st.write(f"**Score:** {r.get('score', 'N/A')}  |  **Time:** {r.get('cook_time', 'N/A')} minutes")
            st.write("Ingredients:", ", ".join(r.get("ingredients", [])))

    # Grocery list button
    if st.button("Generate Grocery List"):
        res = requests.post(f"{API}/grocerylist", json={"ingredients": st.session_state["ing_list"]})
        gl = res.json().get("grocery_list", [])
        st.subheader("Grocery List")
        st.write(", ".join(gl))

    # Meal plan button
    if st.button("Generate 7-day Meal Plan"):
        res = requests.post(f"{API}/mealplan", json={"ingredients": st.session_state["ing_list"]})
        st.subheader("Meal Plan")
        st.text_area("Meal Plan :", value=res.json().get("meal_plan", ""), height=300)

    # Nutrition chart (if calories field present)
    df = pd.DataFrame(st.session_state["results"])
    if not df.empty and "calories" in df.columns:
        fig = px.bar(df, x="title", y="calories", title="Calories per Recipe")
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Enter ingredients and click 'Find Recipes' from the sidebar.")
