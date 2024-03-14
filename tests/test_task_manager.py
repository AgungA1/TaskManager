import unittest
from tasks.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager1 = TaskManager('data/tasks.json')
        self.task_manager2 = TaskManager('data/tasks.json')

    def test_singleton_instance(self):
        self.assertIs(self.task_manager1, self.task_manager2)

    def test_add_task(self):
        initial_count = len(self.task_manager1.view_tasks())
        self.task_manager1.add_task({'title': 'Task 2', 'completed': False})
        new_count = len(self.task_manager1.view_tasks())
        self.assertEqual(new_count, initial_count + 1)

    def test_complete_task(self):
        self.task_manager1.add_task({'title': 'Task 2', 'completed': True})
        self.task_manager1.complete_task(0)
        tasks = self.task_manager1.view_tasks()
        self.assertTrue(tasks[0]['completed'])

if __name__ == '__main__':
    unittest.main()
