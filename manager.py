'''Representation of task manager'''

from models import Task
from json_storage import Storage
from exceptions import TaskNotFoundError


class TaskManager():
    def __init__(self, storage: Storage):
        self.storage = storage
        self._tasks: list[Task] = self.storage.load_tasks()
        self._highest_id = self.max_id()

    def get_new_task_id(self) -> int:
        self._highest_id += 1
        return self._highest_id

    def max_id(self) -> int:
        return max((task.task_id for task in self._tasks), default=0)

    def _index_exist(self, index: int) -> bool:
        return 0 <= index < len(self._tasks)
    
    def add(self, task: Task) -> None:
        self._tasks.append(task)
        self.storage.save_tasks(self._tasks)

    def get_all(self) -> list[Task]:
        return self._tasks.copy()

    def get_task_by_position(self, position: int) -> Task:
        index = position - 1

        if not self._index_exist(index):
            raise TaskNotFoundError
        
        return self._tasks[index]
            
    def delete_task_by_position(self, position: int) -> None:
        index = position - 1

        if not self._index_exist(index):
            raise TaskNotFoundError
        
        del self._tasks[index]
        self.storage.save_tasks(self._tasks)

    def change_task_by_position(
            self,
            position: int,
            name: str | None = None,
            description: str | None = None,
            status: str | None = None
    ) -> None:
        task = self.get_task_by_position(position)

        if name is not None:
            task.name = name
        if description is not None:
            task.description = description
        if status is not None:
            task.status = status

        self.storage.save_tasks(self._tasks)

    def mark_as_done_by_position(self, position: int) -> None:
            task = self.get_task_by_position(position)
            task.status = 'done ✔'
            self.storage.save_tasks(self._tasks)
