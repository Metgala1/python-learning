import sqlite3

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()


cursor.execute("""
                CREATE TABLE IF NOT EXISTS accounts (
                    id INTEGER PRIMARY KEY,
                    owner TEXT NOT NULL,
                    balance INTERGER NOT NULL
                )
                """)
connection.commit()

cursor.executemany(
    "INSERT OR IGNORE INTO accounts (id, owner, balance) VALUES (?, ?, ?)",
    [(1, "Alice", 100_000), (2, "David", 20_000)],
)

connection.commit()

cursor.execute("""
               SELECT * FROM accounts
               """)
accounts = cursor.fetchall()
print(accounts)

def transfer(sender_id, receiver_id, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (sender_id,))
    row = cursor.fetchone()
    
    print(row)

    if row is None:
        raise ValueError("Sender not found")

    sender_balance = row[0]

    if sender_balance < amount:
        raise ValueError("Insufficient funds")

    print(f"Sender balance: {sender_balance}")
    
    cursor.execute("""
                   SELECT id FROM accounts WHERE id = ?
                   """,(receiver_id,))
    
    row = cursor.fetchone()
    
    if row is None:
       raise ValueError("Receiver not found")
   
    try:
        cursor.execute(
        "UPDATE accounts SET balance = balance - ? WHERE id = ?",
        (amount, sender_id))
        
        cursor.execute("""
                    UPDATE accounts SET balance = balance + ? WHERE id = ?
                    """, (amount, receiver_id))
        
        connection.commit()
    except:
        connection.rollback()
        raise
        
        

try:
    transfer(1, 2, 999_999_999)
except ValueError as error:
    print(f"Transfer failed: {error}")