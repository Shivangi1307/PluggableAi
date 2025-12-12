def can_handle(text):
    return "weather" in text.lower()

def handle(text):
    return "☀️ Weather API missing, but the plugin system works!"
