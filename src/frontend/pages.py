from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QLineEdit, 
                             QTextEdit)
import requests


class HomePage(QWidget):
    """Page with options."""
    def __init__(self, switch_page_callback):
        super().__init__()
        layout = QVBoxLayout()

        # Button to navigate to the text input page
        go_to_text_input = QPushButton("Go to Text Input Page")
        go_to_text_input.clicked.connect(lambda: 
                                         switch_page_callback("text_input"))
        layout.addWidget(go_to_text_input)

        self.setLayout(layout)


class TextInputPage(QWidget):
    """Page to add and display tasks."""
    def __init__(self, switch_page_callback):
        super().__init__()
        layout = QVBoxLayout()

        # Input field
        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        # Add Task Button
        add_button = QPushButton("Add Task", self)
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)

        # Fetch Tasks Button
        fetch_button = QPushButton("Fetch Tasks", self)
        fetch_button.clicked.connect(self.fetch_tasks)
        layout.addWidget(fetch_button)

        # Display Area
        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        # Back Button
        back_button = QPushButton("Back")
        back_button.clicked.connect(lambda: switch_page_callback("home"))
        layout.addWidget(back_button)

        self.setLayout(layout)

    def add_task(self):
        """Send the task to FastAPI."""
        task_name = self.text_input.text()
        if task_name:
            response = requests.post("http://127.0.0.1:8000/tasks/", 
                                     json={"id": len(task_name), 
                                           "name": task_name})
            if response.status_code == 200:
                self.text_display.setText("Task added successfully!")
            else:
                self.text_display.setText("Error adding task.")
        else:
            self.text_display.setText("No task entered.")

    def fetch_tasks(self):
        """Fetch tasks from FastAPI."""
        response = requests.get("http://127.0.0.1:8000/tasks/")
        if response.status_code == 200:
            tasks = response.json()
            self.text_display.setText("\n".join(
                [f"{task['id']}: {task['name']}" for task in tasks]))
        else:
            self.text_display.setText("Error fetching tasks.")
