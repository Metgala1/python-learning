import os

with open("note.txt" , "r" , encoding="utf-8") as file:
    content = file.read()

print(content)

print(os.getcwd())