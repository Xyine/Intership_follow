from src.backend.models import Task

tasks_db = []


def add_task(task: Task):
    tasks_db.append(task)


def get_tasks():
    return tasks_db
