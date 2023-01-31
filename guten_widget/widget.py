from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, 
    QWidget, QLabel, QLineEdit, QPushButton, QTextEdit)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys
 
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

        # Title Label
        title_label = QLabel("Guten Widget")
        title_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        title_label.setFont( QFont("Calibri", 22) )

        # Description Label
        description_label = QLabel("Enter a book, author, or subject below.")
        description_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        description_label.setFont(QFont("Calibri", 14))

        # Search Layout (with label, icon?, and button)
        search_layout = QHBoxLayout()
        search_edit = QLineEdit("")
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_guten)
        search_layout.addWidget(search_edit)
        search_layout.addWidget(search_button)

        # Results Label
        results_label = QLabel("Book Results")
        self.results_textedit = QTextEdit("")
        results_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        # add our widgets and labels
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addLayout(search_layout)
        layout.addWidget(results_label)
        layout.addWidget(self.results_textedit)
        layout.addStretch()

    def search_guten(self):
        self.results_textedit.setText("Yo, quit pushing my buttons, bruh!")
        

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()