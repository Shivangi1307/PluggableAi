from plugin_router import PluginRouter
from gemini_core import GeminiCore

# Initialize Gemini + Plugin Router
gemini = GeminiCore()
router = PluginRouter(gemini)

TOTAL_TOKENS = 0
GEMINI_TOKENS = 0


def handle_user_input(user_text):
    global TOTAL_TOKENS, GEMINI_TOKENS

    # Step 1: Ask router if any plugin should handle it
    plugin_result = router.route(user_text)

    if plugin_result is not None:
        print("\n[PLUGIN OUTPUT]")
        print(plugin_result)
        return

    # Step 2: Otherwise, use Gemini (this is where 90% tokens are used)
    print("\n[GEMINI OUTPUT]")

    response, tokens_used = gemini.ask_gemini(user_text)

    # Track token usage for hackathon proof
    TOTAL_TOKENS += tokens_used
    GEMINI_TOKENS += tokens_used

    print(response)
    print(f"\n[Token Usage] Gemini: {GEMINI_TOKENS} / Total: {TOTAL_TOKENS}")
    return


if __name__ == "__main__":
    print("🔌 Welcome to Pluggable AI (Powered 90%+ by Gemini)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("👤 You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        handle_user_input(user_input)
