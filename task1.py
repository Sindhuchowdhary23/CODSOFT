import json
import os


def load_tasks():
    if os.path.exits(Task_FILE):
        with open(Task_FILE, "r") as file:
            return json.load(file)
def task_save():
    with open(Task_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
        
tasks = load_tasks()
Task_FILE = "Task.json"
# Function to show the menu
def show_menu():
    print("\n--- To-Do List ---")
    print("1️⃣  ➕ Add  a Task")
    print("2️⃣  📋 View Tasks")
    print("3️⃣  ✅ Mark Task as Done")
    print("4️⃣  🗑️  Delete Task")
    print("5️⃣  🚪 Exit")

# Function to add a new task
def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✅ Done" if task["done"] else "❌ Not Done"
            print(f"{i}. {task['task']} - {status}")

# Function to mark a task as done
def mark_done():
    view_tasks()
    number = int(input("Enter task number to mark as done: "))
    if 1 <= number <= len(tasks):
        tasks[number - 1]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    number = int(input("Enter task number to delete: "))
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Deleted task: {removed['task']}")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please enter a number from 1 to 5.")


    
