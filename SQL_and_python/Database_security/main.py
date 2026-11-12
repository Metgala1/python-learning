#Attack using sql injection
import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute("""
               SELECT * FROM users
WHERE email = '' OR '1'='1' --'
AND password = 'anything'
               """)

#Solution:Parameterized queries

#Wrong
email = "atagweroger2@gmail.com"
query = f"SELECT * FROM users WHERE email = '{email}'"
cursor.execute(query)

#Right
cursor.execute("""
               SELECT * FROM users WHERE email = ?
               """, (email,))

#What about table names and column names
cursor.execute(
    "SELECT * FROM ?",
    ("users",)
)
#Dangerous
sort_column = input("Sort by: ")

query = f"SELECT * FROM users ORDER BY {sort_column}"

cursor.execute(query)

#Do this use an allowlist 

allowed_columns = {
    "name": "name",
    "email": "email",
    "created": "created_at"
}

sort_choice = input("Sort by: ")

column = allowed_columns.get(sort_choice)

if column is None:
    raise ValueError("Invalid sorting option")

query = f"SELECT * FROM users ORDER BY {column}"

cursor.execute(query)

#python3 -m pip install bcrypt
#use bcrypt to harsh passwords

