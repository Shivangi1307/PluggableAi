from google.generativeai import configure, GenerativeModel

# 🔐 READ API KEY FROM ENVIRONMENT (safe)
# Run:  setx GEMINI_API_KEY "your_key_here"   (Windows)
# Or put it in a .env file (recommended)
import os
API_KEY = os.getenv("AIzaSyDopnKc4gSmepCI6RHtZdsUDh0GqKn8lKs", "")

if not API_KEY:
    raise ValueError("❌ No API key found. Set GEMINI_API_KEY environment variable.")

configure(api_key=API_KEY)

model = GenerativeModel("gemini-pro")

def gemini_model(prompt):
    response = model.generate_content(prompt)
    return response.text
