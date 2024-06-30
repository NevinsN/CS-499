from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *

class DialogBox(object):
    def __init__(self, message):
        self.text = message

        self.messageBox = QMessageBox()

        self.messageBox.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.messageBox.setText("<p align='center'>" + self.text)

        self.messageBox.addButton("Got it", QMessageBox.ButtonRole.AcceptRole)

        self.messageBox.setStyleSheet('''QMessageBox {
                                        background-color: #2b2a2a;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 14pt;
                                        border: 1px solid goldenrod;
                                 }
                                    QDialogButtonBox > QPushButton {
                                        background-color: beige;
                                        color: black;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 20pt; 
                                        border: 2px solid goldenrod; 
                                        padding: 10px;             
                                 }
                                    QLabel {
                                        background-color: beige;
                                        min-height: 300px;
                                        min-width: 500px;
                                        border: 2px solid goldenrod;
                                 }''')

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def executeMessageBox(self):
        self.messageBox.exec()

