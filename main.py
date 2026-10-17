from pathlib import Path

folder = Path("documents")

for file_path in folder.glob("*.json"):
    print(file_path)