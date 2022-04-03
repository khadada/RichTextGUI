# Rich Text Notepad GUI 
# Importing necessary modules and classes:
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMessageBox,QTextEdit,QFileDialog,QInputDialog,QFontDialog,QColorDialog)
from PyQt5.QtGui import QIcon, QColor, QTextCursor
from PyQt5.QtCore import Qt

# Create Own Notepad:
class RichNotepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    
    def initialize_ui(self):
        """
        Initialize the window and display its contents to the screen
        """