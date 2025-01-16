from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Internship Tracker")

        # Create a layout
        self.layout = QVBoxLayout()

        # Create a label to display info
        self.info_label = QLabel("Select an option to display info.", self)
        self.layout.addWidget(self.info_label)

        # Create buttons for options
        self.button_1 = QPushButton("Option 1: Task 1", self)
        self.button_1.clicked.connect(self.show_option_1)
        self.layout.addWidget(self.button_1)

        self.button_2 = QPushButton("Option 2: Task 2", self)
        self.button_2.clicked.connect(self.show_option_2)
        self.layout.addWidget(self.button_2)

        self.button_3 = QPushButton("Option 3: Task 3", self)
        self.button_3.clicked.connect(self.show_option_3)
        self.layout.addWidget(self.button_3)

        # Set the layout to a central widget
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def show_option_1(self):
        self.info_label.setText("Option 1: Task 1 information displayed here.")

    def show_option_2(self):
        self.info_label.setText("Option 2: Task 2 information displayed here.")

    def show_option_3(self):
        self.info_label.setText("Option 3: Task 3 information displayed here.")


# Run the application
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
