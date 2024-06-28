''' A unit test for task manager'''
import unittest
import os
from task_manager import Main


class TestTaskManager(unittest.TestCase):
    '''Unittest class for taskmanger'''
    def setUp(self):
        self.file_path = 'test_tasks.json'
        self.task_manager = Main(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_task(self):
        '''tests the add task function'''
        self.task_manager.add_task(99,
                                   "test_subject",
                                   "test_contact",
                                   "test_description")
        task = self.task_manager.get_task_by_id(99)
        self.assertIsNotNone(task)
        self.assertEqual(task.subject, "test_subject")
        self.assertEqual(task.contact, "test_contact")
        self.assertEqual(task.description, "test_description")
        self.assertEqual(task.status, "Ongoing")

    def test_update_task(self):
        '''Tests the update function'''
        self.task_manager.add_task(99,
                                   "test_subject",
                                   "test_contact",
                                   "test_description")
        self.task_manager.update_task(99,
                                      "update_subject",
                                      "update_contact",
                                      "update_description")
        task = self.task_manager.get_task_by_id(99)
        self.assertEqual(task.subject, "update_subject")
        self.assertEqual(task.contact, "update_contact")
        self.assertEqual(task.description, "update_description")

    def test_close_task(self):
        '''Test closing a task'''
        self.task_manager.add_task(99,
                                   "test_subject",
                                   "test_contact",
                                   "test_description")
        self.task_manager.close_task(99)
        task = self.task_manager.get_task_by_id(99)
        self.assertEqual(task.status, "Closed")

    def test_delete_task(self):
        '''Test deleting a task'''
        self.task_manager.add_task(99,
                                   "test_subject",
                                   "test_contact",
                                   "test_description")
        self.task_manager.delete_task(99)
        task = self.task_manager.get_task_by_id(99)
        self.assertIsNone(task)

    def test_save_and_load_tasks(self):
        '''Test save and load'''
        self.task_manager.add_task(99,
                                   "test_subject",
                                   "test_contact",
                                   "test_description")
        self.task_manager.save_tasks()

        # New instance to test save
        new_task_manager = Main(self.file_path)
        task = new_task_manager.get_task_by_id(99)
        self.assertIsNotNone(task)
        self.assertEqual(task.subject, "test_subject")
        self.assertEqual(task.contact, "test_contact")
        self.assertEqual(task.description, "test_description")
        self.assertEqual(task.status, "Ongoing")


if __name__ == '__main__':
    unittest.main()
