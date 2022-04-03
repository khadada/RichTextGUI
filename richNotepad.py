# Rich Text Notepad GUI 
# Importing necessary modules and classes:
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMessageBox,QTextEdit,QFileDialog,QInputDialog,QFontDialog,QColorDialog)
from PyQt5.QtGui import QIcon, QColor, QTextCursor
from PyQt5.QtCore import Qt,QSize

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
        self.setGeometry(100, 100, 600,500)
        self.setWindowTitle("5.1 Rich Text Notepad GUI")
        # set icon to our gui:
        self.setWindowIcon(QIcon("icons/logo.png"))
        # here to resize the logo icon:
        self.setIconSize(QSize(100, 100))
        self.create_notpad_widget()
        self.note_menu()
    
    def create_notpad_widget(self):
        """
        Set the central widget for QMainWindow, which is the QTextEdit widget for notepad.
        """
        self.text_field = QTextEdit()
        self.setCentralWidget(self.text_field)
    
    
    def note_menu(self):
        """
        Create menu for notepad GUI.
        """
        # Create actions for file menu:
        # New
        new_action = QAction('icons/new_file.png','New',self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.clear_text)
        
        # Open:
        open_action = QAction('icons/open_file.png','Open',self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        
        # Save:
        save_action = QAction('icons/save_file.png','Save',self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        
        # Exit:
        exit_action = QAction('icons/exit.png','Exit',self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

# Run Program:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    note_pad = RichNotepad()
    sys.exit(app.exec_())