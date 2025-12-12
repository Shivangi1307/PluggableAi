from gemini_core import gemini_model

def can_handle(text):
    return any(x in text.lower() for x in ["quiz", "flashcard", "mcq", "questions on"])

def handle(text):
    topic = text.replace("quiz", "").replace("flashcard", "").strip()
    prompt = f"Create 5 flashcards/questions for students on: {topic}"
    return gemini_model(prompt)
