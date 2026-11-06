
import sqlite3

connection = sqlite3.connect("migration_demo.db")

# Find the current database version.
current_version = connection.execute(
    "PRAGMA user_version"
).fetchone()[0]


# Migration 1
if current_version < 1:
    with connection:
        connection.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)

        connection.execute("PRAGMA user_version = 1")


# Migration 2
current_version = connection.execute(
    "PRAGMA user_version"
).fetchone()[0]

if current_version < 2:
    with connection:
        connection.execute("""
            ALTER TABLE users
            ADD COLUMN display_name TEXT
        """)

        connection.execute("""
            UPDATE users
            SET display_name = name
            WHERE display_name IS NULL
        """)

        connection.execute("PRAGMA user_version = 2")


connection.close()
