import json

student = {
    "name": "Roger",
    "age": 23,
    "country": "Cameroon",
    "skills": ["Python", "JavaScript", "React"]
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("Student data saved!")