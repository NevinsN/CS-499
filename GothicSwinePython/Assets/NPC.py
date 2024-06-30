import Assets.Item as Item

class NPC(object):
    def __init__(self, npcDict):
        self.apparel = Item.Item("apparel")
        self.accessory = Item.Item("accessory")
        self.flair = Item.Item("flair")
        self.hintToGive = ''
        self.characterName = npcDict.get('name')

    def setCharacterName(self, characterName):
        self.characterName = characterName

    def getCharacterName(self):
        return self.characterName
    
    def setApparel(self, apparel):
        self.apparel = apparel

    def getApparel(self):
        return self.apparel
    
    def setAccessory(self, accessory):
        self.accessory= accessory

    def getAccessory(self):
        return self.accessory
    
    def setFlair(self, flair):
        self.flair = flair

    def getFlair(self):
        return self.flair
    
    def setHintToGive(self, hintToGive):
        self.hintToGive = hintToGive

    def getHintToGive(self):
        return self.hintToGive
    
    def printCharacterData(self):
        print(self.getCharacterName()) 
        print(self.getAccessory().getWholeItem()) 
        print(self.getApparel().getWholeItem()) 
        print(self.getFlair().getWholeItem())
        print(self.getHintToGive())
        print(self.getGuiltyHintList())