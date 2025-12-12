def can_handle(text):
    return "calculate gpa" in text.lower()

def handle(text):
    grades_text = text.split(":")[-1].strip()
    grade_list = [g.strip().upper() for g in grades_text.split(",")]

    points = {
        "A+": 10, "A": 9,
        "B+": 8, "B": 7,
        "C+": 6, "C": 5,
        "D": 4, "F": 0
    }

    total = sum(points.get(g, 0) for g in grade_list)
    gpa = total / len(grade_list)

    return f"📘 GPA: {round(gpa, 2)}"
