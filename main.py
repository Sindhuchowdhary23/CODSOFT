from menu import display_menu, get_user_choice
from task_manager import add_task, delete_task, mark_done, show_tasks
from storage import load_tasks, save_tasks

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == 2:
            index = int(input("Enter task index to delete: "))
            delete_task(tasks, index)
        elif choice == 3:
            index = int(input("Enter task index to mark as done: "))
            mark_done(tasks, index)
        elif choice == 4:
            show_tasks(tasks)
        elif choice == 5:
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()