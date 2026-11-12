import sqlite3

backup = sqlite3.connect("app_backup.db")
destination = sqlite3.connect("restored_app.db")

try:
    backup.backup(destination)
    print("Database restored successfullt")
finally:
    destination.close()
    backup.close()