import datetime
tasks = []
# Function to show the menu
def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

# Function to add a new task
def add_task():
    task = input("Enter a new task: ")
    due = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
    try:
        due_date = datetime.datetime.strptime(due, "%Y-%m-%d").date() if due else None
    except ValueError:
        print("Invalid date format. Skipping due date.")
        due_date = None
    tasks.append({"task": task, "done": False})
    print("Task added!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            due = f" | Due: {task['due']}" if task.get("due") else ""
            print(f"{i}. {task['task']} - {status}{due}")

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


    
