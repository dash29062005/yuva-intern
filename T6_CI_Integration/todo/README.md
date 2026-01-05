## Problem Statement

This project implements a command-line based To-Do List Manager that allows users to manage tasks directly from the terminal. The application is designed for users who prefer lightweight, fast tools without a graphical interface. A CLI-based solution is suitable because it enables quick task management, scripting potential, and minimal system overhead while maintaining persistent task storage.


## Features

- Add tasks with a title, priority, and optional estimated duration
- Update existing task details
- Mark tasks as completed
- Delete tasks by ID
- List all tasks or filter by completed or pending status
- Persistent task storage using a JSON file


## Project Structure
```text
todo/
├── main.py             # CLI input/command parsing
├── task.py             # Task class (OOP)
├── task_manager.py     # Functions that operate on tasks
├── storage.py          # JSON file read/write helpers
├── tasks.json          # Created automatically
└── README.md
```
## How to Run the Application

Ensure Python 3.8 or higher is installed.

Navigate to the project directory and run commands using the following format:

```bash
python main.py <command> [options]
```

### Add a Task
```bash
python main.py add "Study Python" -p high -d "45 minutes"
```
### Update a Task
```bash
python main.py update 1 -t "Study OOP Concepts" -p mid
```
### Mark a Task as Completed
```bash
python main.py complete 1
```
### Delete a Task
```bash
python main.py delete 1
```
### List Tasks
```bash
python main.py list
python main.py list --completed
python main.py list --pending
```
### View Available Commands

The CLI provides built-in help using argparse:
```bash
python main.py --help
python main.py add --help
```
## Design Decisions

### Task Class
Each task is represented using a dedicated `Task` class to apply object-oriented principles. The class is responsible only for maintaining task data, validating fields, and converting between object and dictionary representations. This ensures clean encapsulation and prevents business logic from leaking into the data model.

### Storage Module
Tasks are persisted using a JSON file to keep the application lightweight and dependency-free. The `storage.py` module handles file initialization, loading, saving, and validation of stored data without performing any task-related logic.

### Task Manager
The `task_manager.py` module acts as the business logic layer. It coordinates task creation, updates, deletion, and completion by interacting with both the Task objects and the storage layer.

### Command-Line Interface
The `main.py` file implements the CLI using Python’s `argparse` module. It is responsible only for parsing user input, routing commands, and displaying output, keeping the interface layer separate from application logic.

## Manual Testing — Terminal Commands

The following commands were used to manually test the application functionality.

### 1. Add multiple tasks with different priorities and durations
```bash
python main.py add "Study Python" -p high -d "45 minutes"
python main.py add "Complete assignment" -p mid -d "2 hours"
python main.py add "Buy groceries" -p low
```
### 2. Update an existing task’s title, priority, and duration
```bash

python main.py update 1 -t "Study Advanced Python" -p mid -d "1 hour"
```
### 3. Attempt to delete a non-existent task ID
```bash

python main.py delete 99
```
Expected: An error message indicating that the task ID does not exist.

### 4. Mark a task as completed
```bash
python main.py complete 2
```
### 5. List tasks and verify filters
```bash
python main.py list
python main.py list --completed
python main.py list --pending
```
### 6. Verify data persistence
```bash
python main.py list
```
Close the terminal, reopen it, and run the command again:

```bash
python main.py list
```
These tests verify correct functionality, error handling, and data persistence.
