import json , os
from pathlib import Path

file_path = Path("note.txt")

content = file_path.read_text(encoding="utf-8")

print(content)