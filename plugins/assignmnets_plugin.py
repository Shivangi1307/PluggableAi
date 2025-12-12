import json
import os

FILE = "assignments.json"

def load():
    if os.path.exists(FILE):
        return json.load(open(FILE))
    return []

def save(data):
    json.dump(data, open(FILE, "w"), indent=2)

def can_handle(text):
    return any(x in text.lower() for x in ["add assignment", "remove assignment", "show assignments"])

def handle(text):
    data = load()

    if "add assignment" in text.lower():
        assignment = text.split("add assignment", 1)[1].strip()
        data.append(assignment)
        save(data)
        return f"Added assignment: {assignment}"

    if "remove assignment" in text.lower():
        assignment = text.split("remove assignment", 1)[1].strip()
        if assignment in data:
            data.remove(assignment)
            save(data)
            return f"Removed assignment: {assignment}"
        return "Assignment not found."

    if "show assignments" in text.lower():
        if not data:
            return "No assignments stored."
        return "Your assignments:\n" + "\n".join(f"- {a}" for a in data)

    return "Invalid assignment command."
