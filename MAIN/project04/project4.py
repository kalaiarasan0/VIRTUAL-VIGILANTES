import os
from datetime import datetime


#file directory
TASKS_FILE_PATH = r"D:\virtual internship\MAIN\project04\tasks.txt"



def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False
    

def load_tasks():
    tasks = {}
    if os.path.exists(TASKS_FILE_PATH):
        with open(TASKS_FILE_PATH, "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 4:
                    date, task, description, completed = parts
                    tasks.setdefault(date, []).append({"task": task, "description": description, "completed": completed.strip().lower() == "true"})
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE_PATH, "w") as file:
        for date, tasks_list in tasks.items():
            for task in tasks_list:
                file.write(f"{date}:{task['task']}:{task['description']}:{task['completed']}\n")

def add_task(tasks, date, task, description):
    tasks.setdefault(date, []).append({"task": task, "description": description, "completed": False})

def view_tasks(tasks):
    for date, tasks_list in tasks.items():
        print(date)
        for index, task in enumerate(tasks_list, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. [{status}] {task['task']} - {task['description']}")
        print()

def view_tasks_mark(tasks_list):
    for index, task in enumerate(tasks_list, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. [{status}] {task['task']} - {task['description']}")
    print()


def mark_task(tasks, date, task_index):
    try:
        tasks[date][task_index]["completed"] = True
        print("Task marked as completed.")
    except IndexError:
        print("Invalid task index. Please try again.")
        return False  # Indicate that the task marking was unsuccessful
    return True  # Indicate that the task marking was successful
    
    


def main():
    tasks = load_tasks()
    
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                date = input("Enter date (DD-MM-YYYY): ")
                if is_valid_date(date):
                    break
                else:
                    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
            task = input("Enter task: ")
            description = input("Enter description: ")
            add_task(tasks, date, task, description)
            save_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            while True:
                date = input("Enter date (YYYY-MM-DD): ")
                if date in tasks:
                    print(date)
                    view_tasks_mark(tasks[date])
                    break
                else:
                    print("No tasks found for the entered date. Please enter a valid date.")
            
            while True:
                task_index = int(input("Enter task index to mark as completed: ")) - 1
                if mark_task(tasks, date, task_index):
                    break # Exit the loop if the task marking was successful
            save_tasks(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
