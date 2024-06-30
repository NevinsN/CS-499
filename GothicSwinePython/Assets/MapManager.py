import random
import pandas as pd
import numpy as np

import Database.DBAccess as DBAccess, Assets.Room as Room, Assets.NPC as NPC
import Data.Hints as Hints

class MapManager(object):
    map = pd.DataFrame({
        0: [None, None, None, None, None],
        1: [None, None, None, None, None],
        2: [None, None, None, None, None],
        3: [None, None, None, None, None],
        4: [None, None, None, None, None]
    })

    def __init__(self):
        self.roomList = []
        self.NPCList = []
        self.villain = None
        self.buildRoomList()
        self.buildMap()
        self.populateConnectedRooms()
        self.pickVillain()
        self.currentRoom = self.roomList[0]

        hintHolder = Hints.generateAndReturnHints(self.villain)
        self.hints = hintHolder[0]
        self.villainHints = hintHolder[1]
        self.assignHints()

    def __del__(self):
        print("Map deleted")

    def setCurrentRoom(self, Room):
        self.currentRoom = Room

    def getCurrentRoom(self):
        return self.currentRoom
    
    def setVillain(self, villain):
        self.villain = villain
    
    def getVillain(self):
        return self.villain

    def buildRoomList(self):
        numRooms = random.randint(9, 13)
        roomImportList = []

        roomDB = DBAccess.DBAccess("Rooms", False)
        roomImportList = roomDB.read({})
        roomDB.closeConnection()

        npcDB = DBAccess.DBAccess("Characters", False)
        ncpImportList = npcDB.read({})
        npcDB.closeConnection()

        for x in range(numRooms + 1):
            newRoom = Room.Room(roomImportList[0])
            roomImportList.pop(0)
            
            newNPC = NPC.NPC(ncpImportList[0])
            ncpImportList.pop(0)

            newRoom.addCharacterToRoom(newNPC)

            self.roomList.append(newRoom)
            self.NPCList.append(newNPC)

            random.shuffle(ncpImportList)
            random.shuffle(roomImportList)

    def buildMap(self):
        previousRoom = None
        for room in self.roomList:
            if room.getRoomName() == "Foyer":
                previousRoom = room
                self.map.loc[4, random.randint(2, 3)] = room
                
                room.setCoords([4, random.randint(2, 3)])
                room.setConnectedRooms(self.calculateConnections(room))

                self.currentRoom = room
            else:
                possiblePositions = self.calculateConnections(previousRoom)
                roomPlaced = False

                while not roomPlaced:
                    for x in range(4):
                        if not possiblePositions:
                            fixRoom = random.choice(self.roomList)
                            possiblePositions = self.calculateConnections(fixRoom)
                            previousRoom = fixRoom
                            print("error catch ran")
                            continue
                        test = random.choice(possiblePositions) 
                        if list(test.keys())[0] == "Invalid Location":
                            continue
                        if list(test.keys())[0] == None:
                            self.map.loc[list(test.values())[0][0], list(test.values())[0][1]] = room
                            room.setConnectedRooms(self.calculateConnections(room))
                            room.setCoords([list(test.values())[0][0], list(test.values())[0][1]])
                            previousRoom = room
                            roomPlaced = True
                            break

                    for connection in possiblePositions:
                        if list(connection.keys())[0] != None:
                            fixRoom = random.choice(self.roomList)
                            possiblePositions = self.calculateConnections(fixRoom)
                            previousRoom = fixRoom

                                                

    def calculateConnections(self, room):
        connectionsList = []
        cellLoc = self.findCellLocationByValue(room)

        for x in range(4):
            newCoords = [5, 5]
            if cellLoc[0] < 0 or cellLoc[0] >= 5 or cellLoc[1] < 0 or cellLoc[1] >= 5:
                continue
            match x:
                case 0:
                    if cellLoc[0] - 1 >= 0:
                        newCoords = [cellLoc[0] - 1, cellLoc[1]]
                        connectionsList.append({self.map.loc[newCoords[0], newCoords[1]]: newCoords})
                    else:
                        connectionsList.append({"Invalid Location": newCoords})
                case 1:
                    if cellLoc[1] + 1 < 5:
                        newCoords = [cellLoc[0], cellLoc[1] + 1]
                        connectionsList.append({self.map.loc[newCoords[0], newCoords[1]]: newCoords})
                    else:
                        connectionsList.append({"Invalid Location": newCoords})
                case 2:
                    if cellLoc[0] + 1 < 5:
                        newCoords = [cellLoc[0] + 1, cellLoc[1]]
                        connectionsList.append({self.map.loc[newCoords[0], newCoords[1]]: newCoords})
                    else:
                        connectionsList.append({"Invalid Location": newCoords})
                case 3:
                    if cellLoc[1] - 1 >= 0:
                        newCoords = [cellLoc[0], cellLoc[1] - 1]
                        connectionsList.append({self.map.loc[newCoords[0], newCoords[1]]: newCoords})
                    else:
                        connectionsList.append({"Invalid Location": newCoords})
        
        return connectionsList
    
    def populateConnectedRooms(self):
        for room in self.roomList:
            room.setConnectedRooms(self.calculateConnections(room))
    
    def findCellLocationByValue(self, room):
        for x in range(5):
            for y in range(5):
                if self.map.loc[x, y] == room:
                    return [x, y]
        return [5, 5]
                
    def findValueByCellLocation(self, cellLocation):
        return self.map.iat[cellLocation[0], cellLocation[1]]
    
    def moveNorth(self):
        newRoom = self.currentRoom.getConnectedRoomByDirection('North')
        self.setCurrentRoom(newRoom[0])

    def moveEast(self):
        newRoom = newRoom = self.currentRoom.getConnectedRoomByDirection('East')
        self.setCurrentRoom(newRoom[0])
    
    def moveSouth(self):
        newRoom = newRoom = self.currentRoom.getConnectedRoomByDirection('South')
        self.setCurrentRoom(newRoom[0])

    def moveWest(self):
        newRoom = newRoom = self.currentRoom.getConnectedRoomByDirection('West')
        self.setCurrentRoom(newRoom[0])

    def printMap(self):
        for col in range(5):
            printString = '| '
            for row in range(5):
                if self.map.loc[col][row] == None:
                    printString += "Empty | "
                else:
                    printString += self.map.loc[col][row].getRoomName() + " | "
            print(printString)
        
    def pickVillain(self):
        self.villain = random.choice(self.NPCList[1 : len(self.NPCList) - 1])

    def assignHints(self):
        newHintsList = [x for x in self.hints]

        random.shuffle(newHintsList)

        for NPC in self.NPCList:
            if NPC.getCharacterName() == self.villain.getCharacterName():
                NPC.setHintToGive(random.choice(self.villainHints))
            else:
                NPC.setHintToGive(newHintsList[0])
                newHintsList.pop(0)