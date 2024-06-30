from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton
from PyQt6.QtCore import *
from functools import partial

class SolveDialogBox(object):
    def __init__(self, charList):
        self.suspectSelection = ''

        self.messageBox = QDialog()

        self.messageBox.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        
        layout = QVBoxLayout()
        
        textLabel = QLabel("Accuse your suspect, but be careful! You only get one guess.")

        selectorLayout = QVBoxLayout()

        for char in charList:
            newRadio = QRadioButton()
            charName = char.getCharacterName()
            newRadio.setText(charName)
            newRadio.toggled.connect(partial(self.changeSuspectSelection, charName))
            selectorLayout.addWidget(newRadio)

        buttonLayout = QHBoxLayout()

        solveButton = QPushButton("They did it!")
        solveButton.clicked.connect(self.submitAccusation)

        cancelButton = QPushButton("On second thought...")        
        cancelButton.clicked.connect(self.messageBox.close)

        buttonLayout.addWidget(solveButton)
        buttonLayout.addWidget(cancelButton)
        layout.addWidget(textLabel)
        layout.addLayout(selectorLayout)
        layout.addLayout(buttonLayout)

        self.messageBox.setStyleSheet('''QDialog {
                                        background-color: #2b2a2a;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 14pt;
                                        border: 1px solid goldenrod;
                                 }
                                    QPushButton {
                                        background-color: beige;
                                        color: black;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 20pt; 
                                        border: 2px solid goldenrod; 
                                        padding: 10px;             
                                 }
                                    QRadioButton {
                                        background-color: beige;
                                        min-height: 30px;
                                        min-width: 50px;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 12pt;
                                        border: 2px solid goldenrod;
                                 }
                                    QLabel {
                                        background-color: beige;
                                        min-height: 30px;
                                        min-width: 50px;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 16pt;
                                        border: 2px solid goldenrod;
                                 }''')
        
        self.messageBox.setLayout(layout)

    def changeSuspectSelection(self, suspect):
        self.suspectSelection = suspect
        print("Player selecting " + self.suspectSelection)

    def getSuspectSelection(self):
        return self.suspectSelection

    def submitAccusation(self):
        self.messageBox.hide()

    def closeWindow(self):
        self.messageBox.close()

    def executeMessageBox(self):
        self.messageBox.exec()