class TaskNotFoundError(Exception):
    pass


def get_task_id():
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
    else:
        return task_id

def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise TaskNotFoundError(
        f"No task exist with ID {task_id}"
    )

def add_task(tasks):
    title = input("Enter task title: ").strip()
    
    if not title:
        print("Task title cannot be empty.")
        return
    
    next_id = max(
        (task["id"] for task in tasks), default=0
    ) + 1
    
    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }
    
    tasks.append(task)
    print(f"Task '{title}' added successfully.")

def complete_task(tasks):
    task_id = get_task_id()
    
    if task_id is None:
        return
    try:
        task = find_task(tasks, task_id)
    except TaskNotFoundError as error:
        print(error)
    else:
        if task["completed"]:
            print("This task is already completed.")
        else:
            task["completed"] = True
            print(f"Task '{task["title"]}' completed")

def view_task(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        status = "completed" if task["completed"] else "pending"
        print(f"ID: {task['id']} | {task['title']} | {status}")
        
def delete_task(tasks):
    task_id = get_task_id()
    if task_id is None:
        return 
    
    try:
        task = find_task(tasks, task_id)
    except TaskNotFoundError as error:
        print(error)
    else:
        tasks.remove(task)
        print(f"Task '{task['title']}' deleted successfully")

def count_pending_task(tasks):
    if not tasks:
        print("No tasks found")
        return
    total_pending = 0
    for task in tasks:
        if task["completed"]:
            continue
        total_pending += 1
    print(f"Total Pending: {total_pending}")
    

def show_menu():
    print("\n===== TASKMASTER =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Total pending tasks")
    print("6. Exit")     

def main():
    tasks = []
    
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            count_pending_task(tasks)
        elif choice == "6":
            print("Exiting program....")
            return
        else:
            print("Invalid menu option. Chooose between 1 and 5")

if __name__ == "__main__":
    main()