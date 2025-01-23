
# Documentation: User Authentication and Task Management System

## Overview
This project is a simple authentication system and task manager built using Python. It allows users to:
1. Register with a username and password.
2. Log in with their credentials.
3. Manage tasks, including adding, viewing, and deleting tasks.
4. Change their password.

The program emphasizes the use of Python basics like dictionaries, loops, and conditional statements.

---

## Features

### Registration
- Users can register with a unique username and password (minimum 6 characters).
- Password validation ensures secure credentials.

### Login
- Users log in with their registered username and password.
- The system validates the input against the user database.

### User Dashboard
After login, users can:
1. View their profile.
2. Change their password.
3. Manage their tasks (add, view, and delete tasks).

### Task Manager
- Add tasks: Users can add descriptions for their tasks.
- View tasks: Lists all tasks added by the user.
- Delete tasks: Removes a specific task by task number.

### Password Management
- Users can update their password after providing the correct current password.
- New passwords are validated to ensure they meet security requirements.

---

## Code Organization

### Main Components
1. **User Registration and Login**:
   - Stores user credentials in a dictionary (`user_database`).
   - Handles input validation for username and password.

2. **Dashboard**:
   - Displays user-specific options after successful login.

3. **Task Manager**:
   - Uses a dictionary (`task_database`) to store tasks for each user.
   - Provides functionality to add, view, and delete tasks.

4. **Password Management**:
   - Ensures secure password updates with validation.

---

## How to Run
1. Save the code as `user_auth_task_manager.py`.
2. Run the file using Python: `python user_auth_task_manager.py`.
3. Follow the on-screen instructions.

---

## Future Enhancements
1. Add functionality for users to update their profiles (e.g., name, address, phone number).
2. Enhance the task manager to allow task editing and prioritization.
3. Implement persistent storage (e.g., using files or a database).

---

## Author
Developed during the RITA Africa Bootcamp.

