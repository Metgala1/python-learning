import sqlite3

source = sqlite3.connect("practice.db")

destination = sqlite3.connect("practice_backup.db")

try:
    source.backup(destination)
    print("Backup completed successfully")
finally:
    destination.close()
    source.close()
    
