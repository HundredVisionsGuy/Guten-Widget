from PyQt6.QtWidgets import (QApplication,QMainWindow, QVBoxLayout, QWidget, 
                             QLabel, QHBoxLayout, QLineEdit,
                             QPushButton, QTextEdit)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (QApplication, QComboBox, QVBoxLayout, QWidget, 
                             QLabel, QHBoxLayout, QLineEdit,
                             QPushButton, QTextEdit)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # Sends the current index (position) of the selected item.
        widget.currentIndexChanged.connect( self.index_changed )

        # There is an alternate signal to send the text.
        widget.currentTextChanged.connect( self.text_changed )

        current_text = widget.currentText()
        print(current_text)
        
        self.setCentralWidget(widget)


    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    # Set Styles
    app.setStyleSheet("""
        QWidget {
            background-color: #99bbdd;
            color: #111111;
            padding: 10px;
        }
        QVBoxLayout {
            padding: 10px;
        }
        QTextEdit {
            border: 0;
        }
        h2 {
            font-size: 70%;
        }
    """)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()