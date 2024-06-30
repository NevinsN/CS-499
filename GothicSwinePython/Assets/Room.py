class Room(object):
    def __init__(self, roomDict):
            self.roomName = roomDict.get("roomName")
            self.roomDescription = roomDict.get("roomDescription")
            self.charactersInRoom = []
            self.connectedRooms = {}
            self.coords = []

    def getRoomID(self):
        return self.roomID
    
    def setRoomName(self, roomName):
        self.roomName = roomName
    
    def getRoomName(self):
        return self.roomName

    def setRoomDescription(self, roomDescription):
        self.roomDescription = roomDescription

    def getRoomDescription(self):
        return self.roomDescription
    
    def setCoords(self, coords):
        self.coords = coords

    def getCoords(self):
        return self.coords
    
    def addCharacterToRoom(self, character):
        self.charactersInRoom.append(character)

    def removeCharacterFromRoom(self, character):
        self.charactersInRoom.remove(character)

    def getCharactersInRoom(self):
        return self.charactersInRoom

    def setConnectedRooms(self, connections):
        connKeys = []
        for conn in connections:
            connKeys.append(list(conn.keys()))
        self.connectedRooms = {
            'North' : connKeys[0],
            'East'  : connKeys[1],
            'South' : connKeys[2],
            'West'  : connKeys[3]
        }

    def getConnectedRooms(self):
        return self.connectedRooms

    def getConnectedRoomByDirection(self, direction):
        return self.connectedRooms.get(direction)

    def getRoomList(self):
        return self.roomList

            
