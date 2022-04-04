# Rich Text Notepad GUI 
# Importing necessary modules and classes:
from json import tool
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMessageBox,QTextEdit,QFileDialog,QInputDialog,QFontDialog,QColorDialog)
from PyQt5.QtGui import QIcon, QColor, QTextCursor
from PyQt5.QtCore import Qt,QSize
from isort import file

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
        
        # ------------------------------------------------
        # Create actions for Edit menu:
        # Undo
        undo_action = QAction('icons/undo.png','Undo',self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.triggered.connect(self.text_field.undo)
        
        # Redo
        redo_action = QAction('icons/redo.png','Redo',self)
        redo_action.setShortcut("Ctrl+Shift+Z")
        redo_action.triggered.connect(self.text_field.redo)
        
        # Cut
        cut_action = QAction('icons/cut.png','Cut',self)
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(self.text_field.cut)
        
        # Copy
        copy_action = QAction('icons/copy.png','Copy',self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.text_field.copy)
        
        # Past
        past_action = QAction('icons/past.png','Past',self)
        past_action.setShortcut("Ctrl+V")
        past_action.triggered.connect(self.text_field.past)
        
        # Find
        find_action = QAction('icons/fing.png','Find',self)
        find_action.setShortcut("Ctrl+F")
        find_action.triggered.connect(self.find_text_dialog)
        # Create actions for Tools menu:
        # Font:
        font_action = QAction("icons/font.png", 'Font', self)
        font_action.setShortcut("Ctrl+T")
        font_action.triggered.connect(self.choose_font)
        
        # Color:
        color_action = QAction("icons/color.png", 'Color', self)
        color_action.setShortcut("Ctrl+Shift+C")
        color_action.triggered.connect(self.choose_font_color)
        
        # Highlight:
        highlight_action = QAction("icons/highlight.png", 'Highlight', self)
        highlight_action.setShortcut("Ctrl+Shift+H")
        highlight_action.triggered.connect(self.hightlight_text)
        
        # Create actions for About menu:
        # About:
        about_action = QAction("icons/about.png", 'About', self)
        about_action.setShortcut("Ctrl+Shift+H")
        about_action.triggered.connect(self.about_us)
        
        #--------------------------------------------
        # ----------- Create MenuBar-----------------
        # Menu bar container:
        menu_bar = self.menuBar()
        # Create File menu & add its action:
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(new_action)
        file_menu.addSeparator()
        file_menu.addAction(open_action)
        file_menu.addSeparator()
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        
        # Create Edit menu & add its action:
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(copy_action)
        edit_menu.addAction(past_action)
        edit_menu.addAction(cut_action)
        edit_menu.addSeparator()
        edit_menu.addAction(find_action)
        
        
        # Create Tools menu & add its action:
        tools_menu = menu_bar.addMenu("Tools")
        tools_menu.addAction(font_action)
        tools_menu.addAction(color_action)
        tools_menu.addAction(highlight_action)
        
        # Create About menu & add its action:
        about_menu = menu_bar.addMenu("About")
        about_menu.addAction(about_action)
        



# Run Program:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    note_pad = RichNotepad()
    sys.exit(app.exec_())