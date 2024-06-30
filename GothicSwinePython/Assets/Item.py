import Database.DBAccess as DBAccess

class Item(object):  
    def __init__(self, type):
        self.type = type
        self.color = None
        self.design = None
        self.baseItem = None

        self.initializeItem()

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setDesign(self, design):
        self.design = design
    
    def getDesign(self):
        return self.design
    
    def setBaseItem(self, baseItem):
        self.baseItem = baseItem

    def getBaseItem(self):
        return self.baseItem
    
    def getWholeItem(self):
        return self.getColor() + " " + self.getDesign() + " " + self.getBaseItem()
        
    def initializeItem(self):
        itemDB = DBAccess.DBAccess("Items", False)
        itemData = itemDB.getRandomSamplingOfValue([
            {'$match': {'type': self.getType()}},
            {'$sample': {'size': 1}}
        ])
        itemDB.closeConnection()

        self.setColor(itemData[0].get('color'))
        self.setDesign(itemData[0].get('design'))
        self.setBaseItem(itemData[0].get('baseItem'))
        
        

