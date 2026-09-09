# Task Manager

A console-based task manager written in Python.

This project was created as a practical project for learning Python,
object-oriented programming, exception handling, type hints,
JSON persistence, unit testing, and basic project structure.

## Features

- Create tasks
- View all tasks
- View a task by position
- Change task name, description, and status
- Mark a task as completed
- Delete tasks
- Automatic task ID generation
- Persistent task storage in JSON
- Handling of missing storage files
- Handling of corrupted JSON storage
- Custom exceptions
- Unit tests for `TaskManager`

## Technologies

- Python 3.10+
- `dataclasses`
- JSON
- `unittest`
- Git

No external Python packages are required.

## Project Structure

```text
task-manager/
├── main.py
├── manager.py
├── models.py
├── json_storage.py
├── exceptions.py
├── tests/
│   └── test_manager.py
├── .gitignore
└── README.md

main.py

Provides the command-line interface.

It is responsible for:

displaying the menu;
reading user input;
validating task positions;
handling application-level exceptions;
calling the appropriate TaskManager methods.
manager.py

Contains the TaskManager class.

It is responsible for managing tasks and implementing the main
application logic:

adding tasks;
retrieving tasks;
deleting tasks;
changing task data;
marking tasks as completed;
generating task IDs.
models.py

Contains the Task dataclass.

The model represents a single task and provides methods for
converting a task to and from a dictionary.

json_storage.py

Contains the Storage class.

It is responsible for persistent storage of tasks in a JSON file.

The storage layer is separated from TaskManager, so the manager
does not need to know how tasks are stored.

exceptions.py

Contains custom application exceptions:

TaskNotFoundError — raised when a requested task does not exist.
StorageCorruptedError — raised when the storage contains invalid JSON.
tests/test_manager.py

Contains unit tests for the main TaskManager operations.

The tests use Python's built-in unittest framework.

Architecture

The project separates responsibilities between the main components:

                    ┌──────────────┐
                    │   main.py    │
                    │      CLI     │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ TaskManager  │
                    │  business    │
                    │    logic     │
                    └──────┬───────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
          ┌────────────┐      ┌────────────┐
          │    Task    │      │  Storage   │
          │   model    │      │ persistence│
          └────────────┘      └─────┬──────┘
                                    │
                                    ▼
                              ┌────────────┐
                              │ JSON file  │
                              └────────────┘

The main responsibilities are separated as follows:

main.py — user interaction;
TaskManager — application logic;
Task — task data model;
Storage — data persistence;
exceptions.py — application-specific errors.
Installation

Clone the repository:

git clone https://github.com/Yurys-hub/task-manager
cd task-manager

No additional dependencies are required.

Make sure Python 3.10 or newer is installed.

Usage

Run the application:

python main.py

The application provides the following commands:

add       Create a new task
open _    Show a task by position
all       Show all tasks
del _     Delete a task
change _  Change a task
done _    Mark a task as completed
exit      Exit the application

For commands containing _, replace _ with the task position.

Example
Welcome to task manager.


Write one of operations:


add: to add one task
open _: where "_" is a number. Use to see full task
all: to see all tasks
del _: to delete task with number "_"
change _: to change task with number "_"
done _: to mark task as done
exit: to quit program


Your choice: add


Task name: Learn Python
Task description: Study classes and exceptions


Task: Learn Python added

Tasks are automatically saved to the JSON storage file.

Testing

The project uses Python's built-in unittest framework.

Run the tests from the project root:

python -m unittest tests.test_manager

The tests cover the main TaskManager operations, including:

checking task indexes;
retrieving tasks;
deleting tasks;
changing task data;
marking tasks as completed.

Error handling for non-existent tasks is also tested.

Error Handling

The application handles several error cases.

Non-existent task

If a requested task does not exist, TaskManager raises:

TaskNotFoundError

The exception is handled by the CLI and an appropriate message is
shown to the user.

Corrupted storage

If the JSON storage file contains invalid JSON,
Storage raises:

StorageCorruptedError

The application catches the exception and informs the user that the
storage file is corrupted.

Missing storage file

If the storage file does not exist, the application starts with an
empty task list.

Project Goals

This project was developed to practice:

Python fundamentals;
object-oriented programming;
dataclasses;
type hints;
exception handling;
separation of responsibilities;
working with JSON persistence;
command-line application design;
unit testing with unittest;
basic Git and GitHub workflow.
Future Development

This console application is the foundation for further backend
development.

The next step is to build a backend version using:

FastAPI;
PostgreSQL;
Docker;
REST API.

The console application itself is considered a completed learning
project.

Git practice. New commands