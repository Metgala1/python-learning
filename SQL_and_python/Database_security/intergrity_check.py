import sqlite3

connection = sqlite3.connect("app.db")

try:
    result = connection.execute(
        "PRAGMA integrity_check"
    ).fetchone()[0]

    if result == "ok":
        print("Database integrity is good.")
    else:
        print("Database integrity problem:", result)

finally:
    connection.close()