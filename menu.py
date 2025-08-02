def display_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add task")
    print("2. Delete task")
    print("3. Mark task as done")
    print("4. Show all tasks")
    print("5. Exit")

def get_user_choice():
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        return None