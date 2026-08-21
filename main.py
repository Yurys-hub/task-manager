'''Using of task manager'''

from manager import TaskManager
from json_storage import Storage
from models import Task
from exceptions import TaskNotFoundError, StorageCorruptedError

def request_task(manager: TaskManager) -> Task:
    task_id = manager.get_new_task_id()
    name = input('Task name: ')
    description = input('Task description: ')
    return Task(task_id, name, description)

def make_position_int(position: str) -> int | None:
    try:
        return int(position)
    except ValueError:
        return None

def show_menu() -> None:
    print(
        '\nadd: to add one task\n'
        'open _: where "_" is a number. Use to see full task\n'
        'all: to see all tasks\n'
        'del _: to delete task with number "_"\n'
        'change _: to change task with number "_"\n'
        'done _: to mark task as done\n'
        'exit: to quit program\n'
    )

def add_task(manager: TaskManager) -> None:
    task = request_task(manager)
    manager.add(task)
    print(f'Task: {task.name} added')

def open_task(manager: TaskManager, position: int) -> None:
    task = manager.get_task_by_position(position)

    print(
        f"\nID: {task.task_id}\n"
        f"Task: {task.name}\n"
        f"Description: {task.description}\n"
        f"Status: {task.status}"
    )

def show_all_tasks(manager: TaskManager) -> None:
    tasks = manager.get_all()
    if tasks:
        for num, task in enumerate(tasks, start=1):
            print(f"{num}. {task.name} {task.status}")
    else:
        print('Tasks list is empty')

def delete_task(manager: TaskManager, position: int) -> None:
    manager.delete_task_by_position(position)

def change_task(manager: TaskManager, position: int) -> None:
    name = None
    description = None
    status = None
    
    open_task(manager, position)
    print(
        'Write attribute you want to change and a new value:\n'
        '• name\n'
        '• description\n'
        '• status\n'
        'or write done to finish'
    )
    while True:
        choice = input('Your choice: ')
        if choice == 'done':
            break
        choice = choice.split(maxsplit=1)
        if len(choice) > 1:
            attribute = choice[0].lower()
            value = choice[1]
            if attribute == 'name':
                name = value
            elif attribute == 'description':
                description = value
            elif attribute == 'status':
                status = value
            else:
                print("Please use only given options")
        else:
            print(f'Please enter an attribute and a new value')
    manager.change_task_by_position(position, name, description, status)

def mark_task_as_done(manager: TaskManager, position: int) -> None:
    manager.mark_as_done_by_position(position)

OPERATIONS = {
    'add' : add_task,
    'open' : open_task,
    'all' : show_all_tasks,
    'del' : delete_task,
    'change' : change_task,
    'done' : mark_task_as_done
}
POSITION_OPERATIONS = {'open', 'del', 'change', 'done'}

def main() -> None:
    try:
        manager = TaskManager(Storage('Storage.json'))
    except StorageCorruptedError:
        print('Storage file is corrupted')
        return

    print('Welcome to task manager.')
    while True:
        input('\nPress Enter to continue...')
        print('Write one of operations:')
        show_menu()
        choice = input('Your choice: ').lower()
        if choice == 'exit':
            break
        choice = choice.split(' ', maxsplit=1)
        operation_key = choice[0]
        if operation_key in OPERATIONS:
            operation = OPERATIONS[operation_key]
            if operation_key in POSITION_OPERATIONS:
                if len(choice) > 1:
                    position = make_position_int(choice[1])
                    if position is not None:
                        try:
                            operation(manager, position)
                        except TaskNotFoundError:
                            print("There's no that task!")
                    else:
                        print('A position has to be a number')
                else:
                    print('That operation takes an argument')
            else:
                operation(manager)
        else:
            print('Please use only given operations.')
            print()

if __name__ == '__main__':
    main()
