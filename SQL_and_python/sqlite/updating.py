
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

try:
    cursor.execute("""
        UPDATE students
        SET age = ?
        WHERE id = ?
    """, (25, 1))

    cursor.execute("""
        DELETE FROM students
        WHERE id = ?
    """, (3,))

    connection.commit()

except sqlite3.Error:
    connection.rollback()
    raise
connection.close()
