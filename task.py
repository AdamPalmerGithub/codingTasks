"""Class Tasks imported for taskmanager"""


class Task:
    '''Task class to define and format attributes used by the class'''
    def __init__(self, task_id, subject,
                 contact, description, status="Ongoing"):

        self.task_id = task_id
        self.subject = subject
        self.contact = contact
        self.description = description
        self.status = status

    def close_task(self):
        '''sets the status to closed'''
        self.status = "Closed"

    def to_dict(self):
        '''Layout to store info'''
        return {
            'task_id': self.task_id,
            'subject': self.subject,
            'contact': self.contact,
            'description': self.description,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        '''retrieve data'''
        return cls(data['task_id'],
                   data['subject'],
                   data['contact'],
                   data['description'],
                   data['status'])

    def __str__(self):
        return (f"ID: {self.task_id}, Subject: {self.subject}, "
                f"Contact: {self.contact}, "
                f"Description: {self.description}, "
                f"Status: {self.status}")
