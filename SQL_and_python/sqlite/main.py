
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

students = [
    ("David", 21, "Cameroon"),
    ("Sarah", 23, "Nigeria"),
    ("John", 20, "Ghana")
]

cursor.executemany("""
    INSERT INTO students (name, age, country)
    VALUES (?, ?, ?)
""", students)

connection.commit()
connection.close()

print("Students inserted successfully!")
