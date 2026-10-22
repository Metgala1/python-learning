from .task import add_task
from .storage import load_task

def main():
    print("Welcome to TaskMaster!")
    tasks = load_task()
    add_task(tasks)

if __name__ == "__main__":
    main()