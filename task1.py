# Define an empty list to store tasks
tasks = []


# Function to add a task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")


# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


# Function to mark a task as completed
def complete_task():
    view_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))

    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task marked as completed.")
    else:
        print("Invalid task number.")


# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")