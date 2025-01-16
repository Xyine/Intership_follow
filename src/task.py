from datetime import datetime


class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        return f"Task(name='{self.name}', due_date='{self.due_date.strftime('%Y-%m-%d')}', completed={self.completed})"
