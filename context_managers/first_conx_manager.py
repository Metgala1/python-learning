with open("python_notes.txt", "w") as file:
    file.write("Context managers make the cleanup safer.")

with open("python_notes.txt", "r") as file:
    content = file.read()

print(content)