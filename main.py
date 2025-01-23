
# user_auth_task_manager.py
"""
User Authentication and Task Management System
Developed as part of the RITA Africa Bootcamp project.
This application allows users to register, log in, manage their profiles, and perform task management operations.
"""

# User database to store registered users
user_database = {}

# Task database to store tasks for each user
task_database = {}


# Function to register a new user
def register_user():
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in user_database:
        print("Username already exists! Try again.")
        return
    password = input("Enter a password (minimum 6 characters): ")
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username] = password
    task_database[username] = []
    print("Registration successful!")


# Function to log in an existing user
def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in user_database:
        print("Username not found! Please register first.")
        return
    password = input("Enter your password: ")
    if user_database[username] == password:
        print(f"Welcome back, {username}!")
        user_dashboard(username)
    else:
        print("Incorrect password! Try again.")


# Dashboard displayed after successful login
def user_dashboard(username):
    while True:
        print(f"\n--- Dashboard: {username} ---")
        print("1. View Profile")
        print("2. Change Password")
        print("3. Manage Tasks")
        print("4. Logout")
        choice = input("Enter your choice (1, 2, 3, or 4): ")
        if choice == "1":
            view_profile(username)
        elif choice == "2":
            change_password(username)
        elif choice == "3":
            task_manager(username)
        elif choice == "4":
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice! Please try again.")


# Function to view user profile
def view_profile(username):
    print(f"\n--- Profile ---")
    print(f"Username: {username}")
    print("Welcome to your dashboard!")


# Function to change password
def change_password(username):
    print("\n--- Change Password ---")
    old_password = input("Enter your current password: ")
    if user_database[username] != old_password:
        print("Incorrect current password! Password not changed.")
        return
    new_password = input("Enter a new password (minimum 6 characters): ")
    if len(new_password) < 6:
        print("Password must be at least 6 characters long!")
        return
    user_database[username] = new_password
    print("Password updated successfully!")


# Task manager to handle tasks
def task_manager(username):
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Go Back to Dashboard")
        choice = input("Enter your choice (1, 2, 3, or 4): ")
        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            delete_task(username)
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")


# Function to add a task
def add_task(username):
    task = input("Enter the task description: ")
    task_database[username].append(task)
    print("Task added successfully!")


# Function to view tasks
def view_tasks(username):
    print("\n--- Your Tasks ---")
    tasks = task_database.get(username, [])
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


# Function to delete a task
def delete_task(username):
    view_tasks(username)
    tasks = task_database.get(username, [])
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Please enter a number.")


# Main program loop
def main():
    while True:
        print("\n--- User Authentication and Task Management System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
