import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from src.frontend.pages import HomePage, TextInputPage


class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.pages = {}

        # Add pages
        self.add_page("home", HomePage(self.switch_page))
        self.add_page("text_input", TextInputPage(self.switch_page))

        self.setCurrentWidget(self.pages["home"])

    def add_page(self, name, widget):
        """Add a page to the stack."""
        self.pages[name] = widget
        self.addWidget(widget)

    def switch_page(self, page_name):
        """Switch to another page."""
        if page_name in self.pages:
            self.setCurrentWidget(self.pages[page_name])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
