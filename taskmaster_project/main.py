# from TaskMaster.task import add_task , view_task , complete_task, delete_task , view_pending_tasks
# from TaskMaster.storage import load_task

#use the comment import or this below as well but this are commit from the __init__.py
from TaskMaster import add_task , view_task , complete_task, delete_task , view_pending_tasks , load_task


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
            view_pending_tasks(tasks)
        elif choice == "6":
            print("Exiting programm..")
            return
        else:
            print("Invalid choice. Please choose between 1 and 5.")
if __name__ == "__main__":
    main()      