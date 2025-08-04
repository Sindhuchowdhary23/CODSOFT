def add_task(tasks, description):
    tasks.append({"description": description, "done": False})
    print(f"Added task: '{description}'")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted task: '{removed['description']}'")
    else:
        print("Invalid task index.")

def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f"Marked task as done: '{tasks[index]['description']}'")
    else:
        print("Invalid task index.")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['description']}")