from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import *

import sys

class WinLossScreen(object):    
    def __init__(self, parent, isVictorious, accusationTarget):
        self.messageBox = QDialog()

        self.parent = parent

        self.messageBox.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        
        layout = QVBoxLayout()
        
        resultLabel = QLabel()
        resultLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        if not isVictorious:
            if accusationTarget == "Constable Eli":
                resultLabel.setText('''
                                    "You think it was me? How could you! You wasted all this time, the
                                    killer is bound to get away! You'll never work again for this!" \n\n
                                    True to the constable's word, you were removed from the police force's
                                    contractor list. To make matters worse, the killer murdered you in your 
                                    sleep several days later, presumably worried you might have information
                                    on them. Too bad. In case you haven't figured it out, Game Over buddy.
                                    ''')
            else:
                resultLabel.setText('''
                                    "Thanks for your hard work! We'll lock them up right away!" \n\n
                                    With all the hustle and bustle of the arrest, the other guests are able 
                                    to slip back to their lives. You receive great acclaim and recognition
                                    for solving such a high profile murder. It feels pretty good, until the
                                    real killer murders you in your sleep. Not only have you expired, but
                                    it seems an innocent might rot in jail too! Better luck next time. Game Over!
                                    ''')
        else:
            resultLabel.setText('''
                                    "Thanks for your hard work! We'll lock them up right away!" \n\n
                                    With all the hustle and bustle of the arrest, the other guests are able 
                                    to slip back to their lives. You receive great acclaim and recognition
                                    for solving such a high profile murder. It feels pretty good, and apparently
                                    {} had a love affair with Abigail that ended poorly. Or maybe it was about money.
                                    Who can keep the details straight? Anyways, you did it! You won! Congrats!
                                    '''.format(accusationTarget))

        buttonLayout = QHBoxLayout()

        #replayButton = QPushButton("Replay")
        #replayButton.clicked.connect(self.replayGame)

        quitButton = QPushButton("Quit")        
        quitButton.clicked.connect(sys.exit)

        #buttonLayout.addWidget(replayButton)
        buttonLayout.addWidget(quitButton)
        layout.addWidget(resultLabel)
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
                                    QLabel {
                                        background-color: beige;
                                        min-height: 30px;
                                        min-width: 50px;
                                        font-family: 'Georgia'; 
                                        font-weight: bold; 
                                        font-size: 12pt;
                                        border: 2px solid goldenrod;
                                 }''')
        
        self.messageBox.setLayout(layout)

        self.messageBox.exec()

    def replayGame(self):
        # TODO FIX ME
        print("TODO: FIX ME")
        