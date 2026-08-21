'''Functions for using storage'''
from json import dump, load, JSONDecodeError

from models import Task
from exceptions import StorageCorruptedError


class Storage():
    def __init__(self, file_name: str = ''):
        self.file_name = file_name

    def save_tasks(self, tasks: list[Task]) -> None:
        if self.file_name:
            tasks_to_save = [task.to_dict() for task in tasks]
            with open(self.file_name, 'w', encoding='utf-8') as f:
                dump(tasks_to_save, f)
            

    def load_tasks(self) -> list[Task]:
        if self.file_name:
            try:
                with open(self.file_name, encoding='utf-8') as f:
                    return [Task.from_dict(data) for data in load(f)]
            except FileNotFoundError:
                return []
            except JSONDecodeError as error:
                raise StorageCorruptedError from error
        return []
