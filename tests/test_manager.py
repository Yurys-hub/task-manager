'''Testing manager methods'''
import unittest

from manager import TaskManager
from models import Task
from json_storage import Storage
from exceptions import TaskNotFoundError, StorageCorruptedError

class TestManagerCase(unittest.TestCase):
    def setUp(self):
        '''Creates and initializes task manager and tasks'''
        self.task_manager = TaskManager(Storage(''))
        # Making first task
        task_id = 1
        name = 'Get some coffee'
        description = 'After breakfast'
        self.task1 = Task(task_id, name, description)
        self.task_manager.add(self.task1)
        # Making second task
        task_id = 2
        name = 'Have a breakfast'
        description = 'At 8 AM'
        self.task2 = Task(task_id, name, description)
        self.task_manager.add(self.task2)

    def test_index_exist(self):
        '''Are indexes stored correctly?'''
        self.assertTrue(self.task_manager._index_exist(0))
        self.assertTrue(self.task_manager._index_exist(1))

        self.assertFalse(self.task_manager._index_exist(-1))
        self.assertFalse(self.task_manager._index_exist(2))

    def test_get_task(self):
        '''Do we get right task?'''
        task1 = self.task1
        task1_from_get = self.task_manager.get_task_by_position(1)
        self.assertEqual(task1, task1_from_get)

    def test_delete_task(self):
        '''Are deleted right task?'''
        deleting_task = self.task1
        self.task_manager.delete_task_by_position(1)
        all_tasks = self.task_manager.get_all()
        self.assertNotIn(deleting_task, all_tasks)

    def test_change_task(self):
        '''Have changed the task?'''
        name = 'Get some cold tea'
        description = 'After a good walk'
        status = 'done ✔'
        self.task_manager.change_task_by_position(
            2,
            name=name,
            description=description,
            status=status
        )
        changed_task_name = self.task_manager.get_task_by_position(2).name
        changed_task_description = self.task_manager.get_task_by_position(2).description
        changed_task_status = self.task_manager.get_task_by_position(2).status
        self.assertEqual(name, changed_task_name)
        self.assertEqual(description, changed_task_description)
        self.assertEqual(status, changed_task_status)

    def test_mark_as_done(self):
        '''Is task marked?'''
        self.task_manager.mark_as_done_by_position(2)
        self.assertEqual(self.task2.status, 'done ✔')

    def test_get_nonexistent_task(self):
        with self.assertRaises(TaskNotFoundError):
            self.task_manager.get_task_by_position(3)

    def test_delete_nonexistent_task(self):
        with self.assertRaises(TaskNotFoundError):
            self.task_manager.delete_task_by_position(-1)

if __name__ == '__main__':
    unittest.main()
