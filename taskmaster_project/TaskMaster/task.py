from .storage import save_tasks


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
    else:
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

def view_pending_tasks(tasks):
    found_pending = False

    for task in tasks:
        if not task["completed"]:
            status = "pending"
            print(f"Task '{task['title']}' is still {status}")
            found_pending = True

    if not found_pending:
        print("No pending tasks.")
