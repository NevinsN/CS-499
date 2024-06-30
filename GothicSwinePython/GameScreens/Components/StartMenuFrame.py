from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import *

import sys

import Database.CreateDBItems as CreateDBItems

class StartMenuFrame(object):
    def __init__(self, parent):
        self.frame = QFrame()

        self.parent = parent

        layout = QVBoxLayout()

        # Game title object
        titleLabel = QLabel("Gothic Swine", self.frame)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titleLabel.setStyleSheet("QLabel {color: goldenrod; font-family: 'Georgia'; font-weight: bold; font-size: 148pt;}")

        # Logic for all the buttons
        buttonLayout = QHBoxLayout()

        startButton = QPushButton("Start Game")
        startButton.clicked.connect(self.startGame)
        startButton.setStyleSheet(self.ReturnTitleButtonCSS())
        
        exitButton = QPushButton("Quit")
        exitButton.clicked.connect(sys.exit)
        exitButton.setStyleSheet(self.ReturnTitleButtonCSS())

        updateItemsButton = QPushButton("Update Items")
        updateItemsButton.clicked.connect(self.updateItemsDatabase)
        updateItemsButton.setStyleSheet(self.ReturnTitleButtonCSS())

        buttonLayout.addWidget(startButton)
        buttonLayout.addWidget(exitButton)

        if self.parent.adminRights:
            buttonLayout.addWidget(updateItemsButton)

        layout.addWidget(titleLabel)
        layout.addLayout(buttonLayout)
        self.frame.setLayout(layout)

        self.frame.hide()

    def setAdminRights(self, adminRights):
        self.adminRights = adminRights

    def getAdminRights(self):
        return self.adminRights
    
    def getFrame(self):
        return self.frame

    def startGame(self):
        '''
        Method to start the game, opening MainWindow and closing this one
        '''
        self.parent.mainWindow.showMaximized()
        self.parent.mainWindow.runIntroDB()

        self.parent.close()

    def ReturnTitleButtonCSS(self):
         '''
         Returns a string to set the push button CSS
         '''
         return """QPushButton {
                height: 75px; 
                max-width: 250px; 
                background-color: #2f2f2f; 
                color: goldenrod; 
                font-family: 'Georgia'; 
                font-weight: bold; 
                font-size: 24pt; 
                border: 2px solid goldenrod; 
                border-radius: 27px}"""
    
    def updateItemsDatabase(self):
        dbInit = CreateDBItems.CreateDBItems("Data/gothicSwineDataItems.csv")