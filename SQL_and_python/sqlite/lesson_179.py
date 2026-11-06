import sqlite3

connection = sqlite3.connect("practice.db")
cursor = connection.cursor()

minimum_salary = 200000
department = "Engineering"

cursor.execute("""
    SELECT *
    FROM employees
    WHERE salary > ?
    AND department = ?
""", (minimum_salary, department))

employees = cursor.fetchall()

for employee in employees:
    print(employee)

connection.close()