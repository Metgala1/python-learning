
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# Retrieve students from Cameroon
cursor.execute(
    "SELECT * FROM students WHERE country = ?",
    ("Cameroon",)
)

students = cursor.fetchall()

# Display the results
for student in students:
    print(student)

connection.close()
