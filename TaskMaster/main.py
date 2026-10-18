import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "tasks.json"

def load_task():
    if not DATA_FILE.exists():
        return []
    
    with DATA_FILE.open("r" , encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks):
    with DATA_FILE.open("w" , encoding="utf-8") as file:
        json.dump(tasks , file , indent=4)

def view_task(tasks):
    if not tasks:
        print("No tasks found")
        return
    print(f"{"=" * 6} YOUR TASK {"="* 6}")
    for task in tasks:
        status = "Completed" if task["completed"] == True else "Pending"
        
        print(f"ID: {task["id"]}")
        print(f"Title: {task["title"]}")
        print(f"Completed: {status}")
        print(f"{"-" * 25}")

def add_task(tasks):
    title = input("Enter the task title: ").strip()
    
    if not title:
        print("Title can not be empty.")
        return
    next_id = max(
        (task["id"] for task in tasks), default=0
    ) + 1
    
    new_task = {
        "id": next_id,
        "title": title,
        "completed": False
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully")

def complete_task(tasks):
    try:
        task_id = int(input("Enter the task ID to complete: "))
    except ValueError:
        print("Please eneter a valid numberic ID.")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("This task is already completed")
                return
            task["completed"] = True
            save_tasks(tasks)
            
            print(f"Task '{task["title"]}' marked as completed!")
            return
    
    print("Task not found")

def delete_task(tasks):
    try:
        task_id = int(input("Enter the task ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID")
        return
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            
            print(f"Tasked '{task["title"]}' deletd successfully")
            return
    print("Task not found")

def view_pending_task(tasks):
    for task in tasks:
        status = "completed" if task["completed"] == True else "pending"
        if not task["completed"]:
            print(f"Task '{task["title"]}' is still {status}")
        else:
            print("No pending task")

def show_menu():
    print("\n========== TASKMASTER ==========")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. View pening tasl")
    print("6. Exit")
    print("================================")
    
def main():
    tasks = load_task()
    
    while True:
        show_menu()
        
        choice = input("Choose an option (1 - 6): ").strip()
        
        if choice == "1":
            view_task(tasks) 
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            view_pending_task(tasks)
        elif choice == "6":
            print("Exiting programm..")
            return
        else:
            print("Invalid choice. Please choose between 1 and 5.")
if __name__ == "__main__":
    main()      