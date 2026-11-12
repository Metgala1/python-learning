import sqlite3
import time

connection = sqlite3.connect("app.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()



start = time.perf_counter()

users = connection.execute(
    "SELECT * FROM users").fetchall()

end = time.perf_counter()

print(f"Query took {end - start:.6f} seconds")