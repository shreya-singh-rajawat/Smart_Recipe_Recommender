# Smart Recipe Recommender
An AI-based meal recommendation system built using **FastAPI** for the backend and **Streamlit** for the frontend.  
This project provides recipe suggestions based on available ingredients, dietary preferences, or meal types.

## Project Overview
- Recommend recipes based on user-provided ingredients.
- Supports dietary preferences (e.g., vegan, keto, gluten-free).
- Backend built with FastAPI for scalable API endpoints.
- Frontend built with Streamlit for an interactive UI.
- Uses AI/ML models for intelligent recipe recommendations.

## Tech Stack
- **Backend:** Python, FastAPI, Uvicorn  
- **Frontend:** Streamlit  
- **AI/ML:** Hugging Face models, OpenAI API  
- **Database:** (if used) SQLite / CSV datasets  
- **Others:** Python virtual environment, pip, requirements.txt

## Model Details
- **Architecture:** [Brief description, e.g., transformer-based or recommendation model]  
- **Data preprocessing:** Cleaning ingredient lists, tokenization, standardizing units  
- **Training:** Model trained on recipe dataset to predict or suggest recipes  
- **Evaluation:** Metrics like accuracy, relevance score, or recommendation ranking  

## Setup Instructions

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/shreya-singh-rajawat/Smart_Recipe_Recommender.git
cd Smart_Recipe_Recommender
Create a virtual environment:

bash
python -m venv venv
source venv/Scripts/activate   

bash
pip install -r requirements.txt
Set environment variables (.env):

env
OPENAI_API_KEY=your_openai_key_here
HF_USER_TOKEN=your_huggingface_token_here
Run the backend:

bash
uvicorn backend.app.main:app --reload
Run the frontend:

bash
streamlit run frontend/app.py

Deliverables
Source code in GitHub repository

Contact
Developed by Shreya Singh Rajawat
GitHub: https://github.com/shreya-singh-rajawat

