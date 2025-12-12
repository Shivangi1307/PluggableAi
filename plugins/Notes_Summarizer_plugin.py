from gemini_core import gemini_model

def can_handle(text):
    return any(x in text.lower() for x in ["summarize", "make short", "explain briefly"])

def handle(text):
    prompt = f"Summarize this for a student:\n{text}"
    return gemini_model(prompt)
