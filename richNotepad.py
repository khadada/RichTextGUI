# Rich Text Notepad GUI 
# Importing necessary modules and classes:
from json import tool
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMessageBox,QTextEdit,QFileDialog,QInputDialog,QFontDialog,QColorDialog)
from PyQt5.QtGui import QIcon, QColor, QTextCursor,QFont
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
        self.text_field.setFont(QFont("Tahoma",15))
        self.setCentralWidget(self.text_field)
    
    
    def note_menu(self):
        """
        Create menu for notepad GUI.
        """
        # Create actions for file menu:
        # New
        new_action = QAction(QIcon('icons/new_file.png'),'New',self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.clear_text)
        
        # Open:
        open_action = QAction(QIcon('icons/open_file.png'),'Open',self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        
        # Save:
        save_action = QAction(QIcon('icons/save_file.png'),'Save',self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        
        # Exit:
        exit_action = QAction(QIcon('icons/exit.png'),'Exit',self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        
        # ------------------------------------------------
        # Create actions for Edit menu:
        # Undo
        undo_action = QAction(QIcon('icons/undo.png'),'Undo',self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.triggered.connect(self.text_field.undo)
        
        # Redo
        redo_action = QAction(QIcon('icons/redo.png'),'Redo',self)
        redo_action.setShortcut("Ctrl+Shift+Z")
        redo_action.triggered.connect(self.text_field.redo)
        
        # Cut
        cut_action = QAction(QIcon('icons/cut.png'),'Cut',self)
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(self.text_field.cut)
        
        # Copy
        copy_action = QAction(QIcon('icons/copy.png'),'Copy',self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.text_field.copy)
        
        # Past
        past_action = QAction(QIcon('icons/past.png'),'Past',self)
        past_action.setShortcut("Ctrl+V")
        past_action.triggered.connect(self.text_field.paste)
        
        # Find
        find_action = QAction(QIcon('icons/find.png'),'Find',self)
        find_action.setShortcut("Ctrl+F")
        find_action.triggered.connect(self.find_text_dialog)
        # Create actions for Tools menu:
        # Font:
        font_action = QAction(QIcon("icons/font.png"), 'Font', self)
        font_action.setShortcut("Ctrl+T")
        font_action.triggered.connect(self.choose_font)
        
        # Color:
        color_action = QAction(QIcon("icons/color.png"), 'Color', self)
        color_action.setShortcut("Ctrl+Shift+C")
        color_action.triggered.connect(self.choose_font_color)
        
        # Highlight:
        highlight_action = QAction(QIcon("icons/highlight.png"), 'Highlight', self)
        highlight_action.setShortcut("Ctrl+Shift+H")
        highlight_action.triggered.connect(self.hightlight_text)
        
        # Create actions for About menu:
        # About:
        about_action = QAction(QIcon("icons/about.png"), 'About', self)
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
    
    # Creating methods and functions
    def open_file(self):
        """
        Open a text or html file and display its contents in the text file area
        """   
        file_name,_ = QFileDialog.getOpenFileName(self,"Open File","","HTML Files (*.html);;Text Files (*.txt)")
        if file_name:
            with open(file_name,'r') as f:
                notpad_txt = f.read()
                self.text_field.setText(notpad_txt)
        else:
            QMessageBox.information(self,"Error","Unable to open file.",QMessageBox.Ok)
    
    def save_file(self):
        """
        if the save button is clicked , display dialog asking user if they want to save the text.
        """    
        file_name,_ = QFileDialog.getSaveFileName(self,"Save File","","HTML Files (*.html);;Text Files (*.txt)")
        if file_name:
            if file_name.endswith(".txt"):
                text = self.text_field.toPlainText()
                with open(file_name,'w') as f:
                    f.write(text)
            elif file_name.endswith(".html"):
                rich_text = self.text_field.toHtml()
                with open(file_name,'w') as f:
                    f.write(rich_text)
    
    def clear_text(self):
        """
        If new button is clicked, display message box asking user if the want to clear the text field.
        """
        answer = QMessageBox.question(self,"Clear Text","Do you want ot clear the text?",QMessageBox.Yes,QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.text_field.clear()
    
    def find_text_dialog(self):
        """
        Search in text QTextEdit widget.
        """
        # Display input dialog ot ask user for text to search for:
        text_search,ok = QInputDialog.getText(self,"Search Text","Find:")
        extra_selections = []
        # Check to make sure the text can be modified:
        if ok and not self.text_field.isReadOnly():
            # Set the cursor in the textEdit field:
            self.text_field.moveCursor(QTextCursor.Start)
            color = QColor(Qt.yellow)
            # Look for next occurrence of text:
            while(self.text_field.find(text_search)):
                # User extraselecton to mark text
                # searching for as yellow:
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(color)
                
                # set the cursor of the selection
                selection.cursor = self.text_field.textCursor()
                
                # Add Selection to list:
                extra_selections.append(selection)
            # Highlight selection in text edit
            for _ in extra_selections:
                self.text_field.setExtraSelections(extra_selections)
    def choose_font(self):
        """
        Selecto font for text
        """
        current = self.text_field.currentFont()
        font,ok = QFontDialog.getFont(current,options=QFontDialog.DontUseNativeDialog ,parent=self)
        if ok:
            self.text_field.setCurrentFont(font) # User setFont to sell all text to one type of font

    def choose_font_color(self):
        """
        Select color for text.
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_field.setTextColor(color)
    
    def hightlight_text(self):
        """
        Select color for text's background.
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_field.setTextBackgroundColor(color)
    
    def about_us(self):
        """
        Display information about the Developer who code this GUI.
        """
        QMessageBox.about(self,"About Notepad","Beginner's Pratical Guid to Create GUI\n\nThis program was create by:Khald Melizi\n\nPhone: +213780360303\n\nEmail:lkhadada@gmail.com\n\nDate:04/04/2022\n\nIn: Temacine W. Touggourt.")
    
        
            
# Run Program:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    note_pad = RichNotepad()
    sys.exit(app.exec_())