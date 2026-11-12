import sqlite3
from pathlib import Path
from datetime import datetime


def backup_database(source_path, backup_directory):
    backup_directory = Path(backup_directory)

    backup_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    backup_path = backup_directory / f"backup_{timestamp}.db"

    source = sqlite3.connect(source_path)
    destination = sqlite3.connect(backup_path)

    try:
        source.backup(destination)
        print(f"Backup created: {backup_path}")

    finally:
        destination.close()
        source.close()


backup_database(
    "app.db",
    "database_backups"
)
