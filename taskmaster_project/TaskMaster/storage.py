import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "tasks.json"

def load_task():
   try:
       with DATA_FILE.open("r" , encoding="utf-8") as file:
           return json.load(file)
   except FileNotFoundError:
       print("No task file exists yet.")
       return []
   except json.JSONDecodeError:
       print("The task file containes invalid JSON.")
       return []

def save_tasks(tasks):
    with DATA_FILE.open("w" , encoding="utf-8") as file:
        json.dump(tasks , file , indent=4)
