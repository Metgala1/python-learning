import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL,
#     country TEXT
# );
# """)

# Index on email for faster lookups
cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)")

# cursor.execute("DELETE FROM users")

# users = [
#     ("Amina Njoya", "amina.njoya@example.com", "Cameroon"),
#     ("Brice Tchoumi", "brice.tchoumi@example.com", "Cameroon"),
#     ("Chidi Okafor", "chidi.okafor@example.com", "Nigeria"),
#     ("Fatou Diop", "fatou.diop@example.com", "Senegal"),
#     ("Kwame Mensah", "kwame.mensah@example.com", "Ghana"),
#     ("Sophie Martin", "sophie.martin@example.com", "France"),
#     ("James Carter", "james.carter@example.com", "United States"),
#     ("Priya Sharma", "priya.sharma@example.com", "India"),
#     ("Lucas Silva", "lucas.silva@example.com", "Brazil"),
#     ("Emma Schmidt", "emma.schmidt@example.com", None),
# ]

# cursor.executemany(
#     "INSERT INTO users (name, email, country) VALUES (?, ?, ?)",
#     users,
# )

# connection.commit()

for row in cursor.execute("SELECT * FROM users"):
    print(row)

connection.close()