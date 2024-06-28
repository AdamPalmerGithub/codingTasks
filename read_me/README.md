This is a Task management application

This programme allows the user to create,update, view, close and delete tasks. This is all used together to form a task
manager so the user can save and update a list of tasks. In creating this programme I learned the importance of separating 
code into multiple classes to help with editing and bug fixing as each class is responsible for a different job. Its like 
having an entire library squashed into one book, it would be very practical so instead you sepearate it into multiple books(classes).
Also I was able to work on and improve my unit testing skills when combined with classes to make sure my code functioned as
expected. Both separating out responsibilities and testing are very important when writing code.

Contents
- tasks.py - task-related attributes and methods to manage task status, convert tasks to and from dictionary format, and provide a string representation.
- task_manager.py - gives functionality to the task manager program with necessary functions using the task.py format.
- test_task_manager - Unit Test for task manager.
- tasks.json - Saves any changes you make to your task manager.
- requirements.txt - A list of requirements to run the code.

Requirements
-Python interpreter
-Flake 8

usage
Once installed, run the code.
-A menu will appear prompting for an input 1-6 to use the wanted function.
 ![alt text](image.png)

1.View Tasks - A list of tasks with the contact and status listed,
to view the description for the task input the task ID
 ![alt text](image-1.png)

The input was 1 so task 1 was shown.

2.Create Task - It will ask for a subject, contact and description, when filled press 'Enter' to move onto the next field. Afterwards it will say 'successfully created' and the new task will be able to be filled.
 ![alt text](image-2.png)

3.Update task - It will list the tasks and request the ID of the task you want to update. Once entered it ask for a new subject, contact and description(pressing 'Enter' to proceed to the next field) if left empty the field won't change.
 ![alt text](image-3.png)

4.Close task - It will list the tasks and ask for the ID of the task you wish to close. When entered it will change the task status to closed instead of ongoing and return to the menu.
![alt text](image-4.png)

5.Delete task - It will list the tasks and ask for the ID of the one you wish to delete. when entered it will return a success message and return to the menu.
![alt text](image-5.png)

6.Logout - It will close the task manager, your tasks will be saved in the tasks.json file for the future.
![alt text](image-6.png)

Credits
- Adam