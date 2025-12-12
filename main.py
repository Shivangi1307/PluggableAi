from plugin_router import PluginRouter
from gemini_core import gemini_model

router = PluginRouter()

print("🔌 Pluggable AI v2 – Powered by Gemini")
print("Type 'exit' to quit.\n")

while True:
    user = input("👤 You: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    # Try plugin first
    plugin_response = router.route(user)

    if plugin_response:
        print("\n[PLUGIN OUTPUT]")
        print(plugin_response)
        print()
        continue

    # Fall back to Gemini
    print("\n[GEMINI OUTPUT]")
    print(gemini_model(user))
    print()
