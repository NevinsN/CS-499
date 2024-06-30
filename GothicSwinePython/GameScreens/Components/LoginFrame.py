from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt6.QtCore import *

class LoginFrame(object):
    def __init__(self, parent):
        self.frame = QFrame()

        self.parent = parent

        layout = QVBoxLayout()

        userButton = QPushButton("Login as User")
        userButton.clicked.connect(self.switchToStartMenu)
        userButton.setStyleSheet(self.ReturnTitleButtonCSS())

        adminButton = QPushButton("Login as Admin")
        adminButton.clicked.connect(self.switchToStartMenuAdmin)
        adminButton.setStyleSheet(self.ReturnTitleButtonCSS())

        layout.addWidget(userButton)
        layout.addWidget(adminButton)
        self.frame.setLayout(layout)

        self.frame.show()
    
    def getFrame(self):
        return self.frame

    def switchToStartMenu(self):
        self.frame.hide()
        self.parent.startMenuFrame.getFrame().show()
        return True
    
    def switchToStartMenuAdmin(self):
        self.parent.adminRights = True

        print(self.parent.adminRights)

        self.frame.hide()
        self.parent.startMenuFrame.getFrame().show()

    def ReturnTitleButtonCSS(self):
         '''
         Returns a string to set the push button CSS
         '''
         return """QPushButton {
                height: 75px; 
                max-width: 300px; 
                background-color: #2f2f2f; 
                color: goldenrod; 
                font-family: 'Georgia'; 
                font-weight: bold; 
                font-size: 24pt; 
                border: 2px solid goldenrod; 
                border-radius: 27px}"""
