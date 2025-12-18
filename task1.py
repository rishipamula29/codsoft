# To-Do List Application in Python

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def update_task():
    show_tasks()
    if tasks:
        num = int(input("\nEnter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter updated task: ")
            tasks[num - 1] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

def delete_task():
    show_tasks()
    if tasks:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
