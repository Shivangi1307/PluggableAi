import importlib
import os

class PluginRouter:
    def __init__(self):
        self.plugins = self.load_plugins()

    def load_plugins(self):
        plugins = []
        for file in os.listdir("plugins"):
            if file.endswith(".py"):
                module_name = file[:-3]
                module = importlib.import_module(f"plugins.{module_name}")

                if hasattr(module, "can_handle") and hasattr(module, "handle"):
                    plugins.append(module)

        return plugins

    def route(self, text):
        for plugin in self.plugins:
            if plugin.can_handle(text):
                return plugin.handle(text)

        return None
