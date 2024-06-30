import sys

from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt6.QtCore import *

import Assets.MapManager as MapManager
import GameScreens.Components.MapDisplayFrame as MapDisplay
import GameScreens.Components.DialogBox as DiBx
import GameScreens.Components.SolveDialogBox as SolvBx
import Assets.PlayerCharacter as PC
import GameScreens.Components.WinLossScreen as WinLoss

class MainWindow(QMainWindow):
    '''
    A class for the main gameplay window

    Attributes:
        layout (QVBoxLayout): The main window layout
        roomName (string): holds the name of the current room
        roomDescription(string): holds the description of the current room
        charactersInRoom (string list): holds the list of characters in the room
        roomText (string): holds the text displayed in the gameplay label
    '''
    layout = QVBoxLayout()

    introText = '''You're finally here! My name is Constable Eli. Late last night, the world-renowned singer Abigail Piper
                   was murdered at her own dinner party in her gothic manor house! She asked everyone to come in their 
                   favorite attire, so we had some bizzare looks! Maybe that will help you narrow down a suspect. <br><br> 
                   I've sequestered each guest in a seperate room, so question them soon as you can. I'm sure the guilty 
                   party will lie, and some of the guests might not be as reliable as we would like. Remember, as a law
                   enforcement officer, I'll always be honest, though I can't promise to be helpful. <br><br>
                   Once you think you know who the fiend is, come back here and let me know! Good luck, detective!<br><br>
                   Oh, and be careful or you might be next!'''

    def __init__(self):
        '''
        Initializes main window
        '''
        super().__init__()

        self.currentRoom = None
        
        # removes window frame
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Gothic Swine")

        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setStyleSheet("QMainWindow {background-color: black}")
        
        self.map = MapManager.MapManager()

        self.player = PC.PlayerCharacter()

        self.currentRoom = self.map.getCurrentRoom()

        # sets the needed label for the room title
        self.roomNameLabel = QLabel(self.currentRoom.getRoomName())
        self.roomNameLabel.setStyleSheet("""QLabel {
                                    color: goldenrod;
                                    font-family: 'Georgia';
                                    font-size: 40pt;
                                    font-weight: bold
                                    }
                                    """)
        
        # holds the top two elements of the screen 
        gameplayLayout = QHBoxLayout()

        # holds layout for the main game screen
        mainScreenLayout = QGridLayout()

        # button to handle going north
        self.goNorthButton = QPushButton("Go North")
        self.goNorthButton.setDisabled(True)
        self.goNorthButton.clicked.connect(self.goNorth)
        self.goNorthButton.setStyleSheet(self.ReturnScreenButtonCSS())

        # add roomNameLabel and goNorthButton to first two rows
        mainScreenLayout.addWidget(self.roomNameLabel, 0, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)
        mainScreenLayout.addWidget(self.goNorthButton, 1, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)

        # button to handle going west
        self.goWestButton = QPushButton("Go West")
        self.goWestButton.setDisabled(True)
        self.goWestButton.clicked.connect(self.goWest)
        self.goWestButton.setStyleSheet(self.ReturnScreenButtonCSS())

        self.gameplayLabel = QLabel()
        self.buildRoomText()

        # gameplayLabel presents the player with the information about the current room
        self.gameplayLabel.setStyleSheet("""QLabel {
                                    background-color: beige;
                                    color: black;
                                    font-family: 'Georgia';
                                    font-size: 14pt;
                                    border: 2px solid goldenrod; 
                                    border-radius: 27px; 
                                    min-height: 400px;
                                    min-width: 500px;}""")
        self.gameplayLabel.setWordWrap(True)
        self.gameplayLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # button to handle going east
        self.goEastButton = QPushButton("Go East")
        self.goEastButton.setDisabled(True)
        self.goEastButton.clicked.connect(self.goEast)
        self.goEastButton.setStyleSheet(self.ReturnScreenButtonCSS())

        # adds center row widgets to mainScreenLayout
        mainScreenLayout.addWidget(self.goWestButton, 2, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)
        mainScreenLayout.addWidget(self.gameplayLabel, 2, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)
        mainScreenLayout.addWidget(self.goEastButton, 2, 2, 1, 1, Qt.AlignmentFlag.AlignCenter)

        # button to handle going south
        self.goSouthButton = QPushButton("Go South")
        self.goSouthButton.setDisabled(True)
        self.goSouthButton.clicked.connect(self.goSouth)
        self.goSouthButton.setStyleSheet(self.ReturnScreenButtonCSS())

        # add goSouthButton to layout
        mainScreenLayout.addWidget(self.goSouthButton, 3, 1, 1, 1, Qt.AlignmentFlag.AlignCenter)

        self.initRoomButtons()

        # adds mainScreenLayout to gamePlayLayout
        gameplayLayout.addLayout(mainScreenLayout)

        background = QWidget()
        background.setStyleSheet("""QWidget {
                                 background-color: beige;
                                 max-height: 600px;
                                 border: 2px solid goldenrod; 
                                 border-radius: 27px
                                 }
                                 """)
        

        # menuLayout holds menu buttons vertically
        menuLayout = QVBoxLayout(background)
        menuLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # menu button logic
        self.notepadButton = QPushButton("Notes")
        self.notepadButton.clicked.connect(self.checkNotepad)
        self.notepadButton.setStyleSheet(self.ReturnScreenButtonCSS())
        self.notepadButton.setDisabled(True)

        examineNPCButton = QPushButton("Examine Person")
        examineNPCButton.clicked.connect(self.examineCharacterInRoom)
        examineNPCButton.setStyleSheet(self.ReturnScreenButtonCSS())

        questionNPCButton = QPushButton("Question Person")
        questionNPCButton.clicked.connect(self.questionCharacter)
        questionNPCButton.setStyleSheet(self.ReturnScreenButtonCSS())

        self.solveButton = QPushButton("Attempt to Solve")
        self.solveButton.clicked.connect(self.attemptToSolveGame)
        self.solveButton.setStyleSheet(self.ReturnScreenButtonCSS())
        self.solveButton.setDisabled(True)

        quitButton = QPushButton("Quit")
        quitButton.clicked.connect(sys.exit)
        quitButton.setStyleSheet(self.ReturnScreenButtonCSS())

        menuLayout.addWidget(self.notepadButton)
        menuLayout.addWidget(examineNPCButton)
        menuLayout.addWidget(questionNPCButton)
        menuLayout.addWidget(self.solveButton)
        menuLayout.addWidget(quitButton)

        gameplayLayout.addWidget(background)

        # sets cursor
        cursor = Qt.CursorShape.PointingHandCursor
        self.setCursor(cursor)

        mapDisplay = MapDisplay.MapDisplayFrame(self.map.map)
        mapFrame = mapDisplay.getFrame()

        # finalizes layout and app display
        self.layout.addLayout(gameplayLayout)
        self.layout.addWidget(mapFrame)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def setAdminRights(self, adminRights):
        self.adminRights = adminRights

    def getAdminRights(self):
        return self.adminRights

    def ReturnScreenButtonCSS(self):
        '''
        Method to return CSS for the QPushButtons
        '''
        return """QPushButton {
                min-height: 40px; 
                min-width: 125px; 
                background-color: #2f2f2f; 
                color: goldenrod; 
                font-family: 'Georgia'; 
                font-weight: bold; 
                font-size: 16pt; 
                border: 2px solid goldenrod; 
                border-radius: 27px;
                padding: 5px}
                
                QPushButton:disabled {
                color: gray;
                }"""
    
    def buildRoomText(self):
         '''
         Method to build the text for the gameplayLabel
         '''
         self.roomNameLabel.setText(self.currentRoom.getRoomName())
         textToReturn = self.currentRoom.getRoomDescription()
         textToReturn += "\n\nOther people in the room: "
         for char in self.currentRoom.getCharactersInRoom():
             textToReturn += char.getCharacterName()

         self.gameplayLabel.setText(textToReturn)
    
    def initRoomButtons(self): 
        self.goSouthButton.setDisabled(True)
        self.goNorthButton.setDisabled(True)
        self.goEastButton.setDisabled(True)
        self.goWestButton.setDisabled(True)
   
        for direction, room in self.currentRoom.getConnectedRooms().items():
            if room == ["Invalid Location"]:
                continue
            elif room == [None]:
                continue
            else:
                match direction:
                    case 'North':
                        self.goNorthButton.setDisabled(False)
                    case 'East':
                        self.goEastButton.setDisabled(False)
                    case 'South':
                        self.goSouthButton.setDisabled(False)
                    case 'West':
                        self.goWestButton.setDisabled(False)                      

    def goNorth(self):
        self.map.moveNorth()
        self.currentRoom = self.map.getCurrentRoom()
        
        self.buildRoomText()
        self.initRoomButtons()

        if self.currentRoom.getRoomName() == 'Foyer':
            self.solveButton.setDisabled(False)
        else:
            self.solveButton.setDisabled(True)

        print("Moved to the " + str(self.currentRoom.getRoomName()))

    def goEast(self):
        self.map.moveEast()
        self.currentRoom = self.map.getCurrentRoom()

        self.buildRoomText()
        self.initRoomButtons()

        if self.currentRoom.getRoomName() == 'Foyer':
            self.solveButton.setDisabled(False)
        else:
            self.solveButton.setDisabled(True)
        
        print("Moved to the " + str(self.currentRoom.getRoomName()))

    def goSouth(self):
        self.map.moveSouth()
        self.currentRoom = self.map.getCurrentRoom()

        self.buildRoomText()
        self.initRoomButtons()

        if self.currentRoom.getRoomName() == 'Foyer':
            self.solveButton.setDisabled(False)
        else:
            self.solveButton.setDisabled(True)
        
        print("Moved to the " + str(self.currentRoom.getRoomName()))

    def goWest(self):
        self.map.moveWest()
        self.currentRoom = self.map.getCurrentRoom()

        self.buildRoomText()
        self.initRoomButtons()

        if self.currentRoom.getRoomName() == 'Foyer':
            self.solveButton.setDisabled(False)
        else:
            self.solveButton.setDisabled(True)
        
        print("Moved to the " + str(self.currentRoom.getRoomName()))

    def examineCharacterInRoom(self):
        dialogBox = DiBx.DialogBox(self.player.examineCharacter(self.currentRoom.getCharactersInRoom()[0]))
        dialogBox.executeMessageBox()

    def questionCharacter(self):
        dialogBox = DiBx.DialogBox(self.currentRoom.getCharactersInRoom()[0].getHintToGive())
        self.player.questionCharacter(self.currentRoom.getCharactersInRoom()[0])
        dialogBox.executeMessageBox()

        self.notepadButton.setDisabled(False)

    def checkNotepad(self):        
        notes = self.player.getNotes()
        notepadString = ''
        for charNPC, hint in notes.items():
            notepadString += charNPC.getCharacterName() + ": " + hint + "<br>"

        dialogBox = DiBx.DialogBox(notepadString)
        dialogBox.executeMessageBox()

    def attemptToSolveGame(self):
        slvBox = SolvBx.SolveDialogBox(self.map.NPCList)
        slvBox.executeMessageBox()
        playerAccusation = slvBox.getSuspectSelection()
        slvBox.closeWindow()
        if playerAccusation == self.map.getVillain().getCharacterName():
            print("You won!")
            winLoss = WinLoss.WinLossScreen(self, True, playerAccusation)

        else:
            print("You lost!")
            winLoss = WinLoss.WinLossScreen(self, False, playerAccusation)

    def runIntroDB(self):
        introDB = DiBx.DialogBox(self.introText)
        introDB.executeMessageBox()