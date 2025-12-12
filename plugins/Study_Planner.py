from gemini_core import gemini_model

def can_handle(text):
    return any(x in text.lower() for x in ["study plan", "timetable", "schedule"])

def handle(text):
    prompt = f"Create a simple study plan for this student request:\n{text}"
    return gemini_model(prompt)
