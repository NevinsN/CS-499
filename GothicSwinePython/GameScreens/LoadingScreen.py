from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton
from PyQt6.QtCore import *
from functools import partial

class SolveDialogBox(object):
    def __init__(self):
        self.messageBox = QDialog()

        self.messageBox.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        
        layout = QVBoxLayout()
        
        textLabel = QLabel("Starting Game... Please Wait...")

        layout.addWidget(textLabel)

        self.messageBox.setStyleSheet('''QDialog {
                                        background-color: #2b2a2a;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 14pt;
                                        border: 1px solid goldenrod;
                                 }
                                    
                                    QLabel {
                                        background-color: beige;
                                        min-height: 30px;
                                        min-width: 50px;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 36pt;
                                        border: 2px solid goldenrod;
                                 }''')
        
        self.messageBox.setLayout(layout)

    def closeWindow(self):
        self.messageBox.close()

    def executeMessageBox(self):
        self.messageBox.exec()