from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QWidget, 
                             QLabel, QHBoxLayout, QLineEdit,
                             QPushButton, QTextEdit)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys
import controller
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 400)
        self.setWindowTitle("The Guten-widget")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.UI()

    def UI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        # Create our Widgets
        title_label = QLabel("Guten Search Widget")
        title_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        title_label.setFont(QFont("Calibri", 22))
        
        description = "Search the Gutenberg Project by title,"
        description += " author, or subject."
        description_label = QLabel(description)
        description_label.setFont(QFont("Calibri", 14))
        
        search_layout = QHBoxLayout()
        self.search_field = QLineEdit()
        self.search_field.setFont(QFont("Calibri", 12))
        self.search_field.setPlaceholderText("title, author, or subject")
        
        search_button = QPushButton("Search")
        search_button.setFont(QFont("Calibri", 12))
        search_button.clicked.connect(self.search)
        
        search_layout.addWidget(self.search_field)
        search_layout.addWidget(search_button)
        
        self.results_text = QTextEdit("Results.")
        self.results_text.setFont(QFont("Calibri", 12))

        # Add all our widgets
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addLayout(search_layout)
        layout.addWidget(self.results_text)

    def search(self):
        """get the search text and use it to make an API call to get
        the results for a search"""
        # get the user input
        search_text = self.search_field.text()

        # Make an API call with the controller script
        search_results = controller.make_call(search_text)
        self.results_text.setText(search_results)
        self.results_text.toHtml()
        
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()