'''This is a task manager program for creating, viewing, updating,
 closing and deleting '''

import json
from task import Task


class Main:
    '''Task manager class to contain functions to interact with the task
    class attributes.'''
    def __init__(self, file_path='tasks.json'):
        self.file_path = file_path
        self.task_lst = self.load_tasks()

    def add_task(self, task_id, subject, contact, description):
        '''funtcion to add a task to the file'''
        self.task_lst.append(Task(task_id, subject, contact, description))
        self.save_tasks()

    def view_tasks(self):
        '''function to view task id, subject and contact'''
        for task in self.task_lst:
            print(f"""ID: {task.task_id},
                Subject: {task.subject},
                Contact: {task.contact},
                Status: {task.status}""")

    def list_tasks(self):
        '''function to list the tasks, used with other functions'''
        for task in self.task_lst:
            print(f"""Task {task.task_id}:
- {task.subject}. - {task.contact}. Status: {task.status}.""")

    def update_task(self, task_id, subject=None, contact=None,
                    description=None):
        '''function to edit the details or a task once created,
          works with the list function'''
        task = self.get_task_by_id(task_id)
        if task:
            if subject is not None:
                task.subject = subject
            if contact is not None:
                task.contact = contact
            if description is not None:
                task.description = description
            self.save_tasks()
            print("Task updated successfully.")
        else:
            print("Task not found")

    def close_task(self, x):
        '''Function to change tasks from ongoing to closed'''
        task = self.get_task_by_id(x)
        if task:
            task.close_task()
            self.save_tasks()
            print("Task closed successfully.")
        else:
            print("Task not found")

    def delete_task(self, x):
        '''function to delete tasks once listed'''
        task = self.get_task_by_id(x)
        if task:
            self.task_lst.remove(task)
            self.save_tasks()
            print("Task deleted successfully.")
        else:
            print("Invalid task ID.")

    def read_tasks(self, x):
        '''function to read a task once listed'''
        i = self.get_task_by_id(x)
        if i:
            print(f"""Subject: {i.subject}\n
            Contact: {i.contact}\n
            Description: {i.description}\n
            Status: {i.status}""")
        else:
            print("No ID found")

    def get_task_by_id(self, task_id):
        '''Function to use the task id rather than its index'''
        for task in self.task_lst:
            if task.task_id == task_id:
                return task
        return None

    def save_tasks(self):
        '''Function to save tasks to a file'''
        with open(self.file_path, 'w', encoding="UTF-8") as file:
            tasks_data = [task.to_dict() for task in self.task_lst]
            json.dump(tasks_data, file, indent=4)

    def load_tasks(self):
        '''Function to load tasks from a file'''
        try:
            with open(self.file_path, 'r', encoding="UTF-8") as file:
                tasks_data = json.load(file)
                return [Task.from_dict(data) for data in tasks_data]
        except FileNotFoundError:
            return []


task_manager = Main()
'''Creating an instance of task manager '''

# task_manager.add_task(1, "Friday meeting",
#  "John Doe", "Meeting about magic")  # examples
# task_manager.add_task(2, "Lunch thief",
#  "steve mc'queen", "I know you keep stealing my lunch John")

while True:
    try:
        # The menu the user interacts that calls functions previosly defined
        choice = int(input("Choose an option from the following: \n"
                           "1. view tasks\n"
                           "2. create a task\n"
                           "3. update a task\n"
                           "4. close a task\n"
                           "5. delete a task\n"
                           "6. logout\n"))

        if choice == 1:
            task_manager.list_tasks()
            task_manager.read_tasks(int(input(
                "Please input a number to see the task: ")))

        elif choice == 2:
            user_input_subject = input("Enter subject: ")
            user_input_contact = input("Enter contact: ")
            user_input_description = input("Enter description: ")
            task_manager.add_task(len(task_manager.task_lst) + 1,
                                  user_input_subject,
                                  user_input_contact,
                                  user_input_description)
            print("Task added successfully.")

        elif choice == 3:
            task_manager.list_tasks()
            user_input_task_id = int(input(
                "Enter the task ID you want to update: "))
            user_input_subject = input(
                "Enter new subject (press enter to keep current): ") or None
            user_input_contact = input(
                "Enter new contact (press enter to keep current): ") or None
            user_input_description = input(
                "Enter new description (press enter to keep current): ") or None
            task_manager.update_task(user_input_task_id,
                                     user_input_subject,
                                     user_input_contact,
                                     user_input_description)

        elif choice == 4:
            task_manager.list_tasks()
            user_input_task_id = int(input(
                "Enter the task ID of the task to close: "))
            if task_manager.close_task(user_input_task_id):
                print("Task closed successfully.")
            else:
                print("Task ID not found. No task was closed.")

        elif choice == 5:
            task_manager.list_tasks()
            task_index = int(input("Enter the ID of the task to delete: "))
            task_manager.delete_task(task_index)

        elif choice == 6:
            print("Logging out...")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    '''Dosent run when exported'''
    program = Main()
    program.view_tasks()


if __name__ == "__main__":
    main()
