from google.generativeai import configure, GenerativeModel

configure(api_key="")

class GeminiCore:
    def __init__(self):
        self.model = GenerativeModel("gemini-pro")

    def ask_gemini(self, prompt):
        response = self.model.generate_content(prompt)

        # For token tracking — approximate
        tokens_used = len(prompt.split()) + len(response.text.split())

        return response.text, tokens_used
