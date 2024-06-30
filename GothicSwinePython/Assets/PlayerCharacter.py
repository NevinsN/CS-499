
class PlayerCharacter(object):
    def __init__(self):
        self.notes = {}
        self.location = None

    def appendToNotes(self, noteDictionary):
        self.notes.update(noteDictionary)

    def getNotes(self):
        return self.notes

    def setLocation(self, room):
        self.location = room

    def getLocation(self):
        return self.location
    
    def examineCharacter(self, npc):
        textToReturn = npc.getCharacterName()
        if npc.getApparel().getWholeItem()[len(npc.getApparel().getWholeItem()) - 1:] == 's':
            textToReturn += " is wearing "
        elif self.isVowel(npc.getApparel().getWholeItem()[0]):
            textToReturn += " is wearing an "
        else:
            textToReturn += " is wearing a "
        textToReturn += npc.getApparel().getWholeItem()
        
        if npc.getAccessory().getWholeItem()[len(npc.getAccessory().getWholeItem()) - 1:] == 's':
            textToReturn += ", "
        elif self.isVowel(npc.getAccessory().getWholeItem()[0]):
            textToReturn += ", an "
        else:
            textToReturn += ", a "
        textToReturn += npc.getAccessory().getWholeItem()

        if npc.getFlair().getWholeItem()[len(npc.getFlair().getWholeItem()) - 1:] == 's':
            textToReturn += ", and "
        elif self.isVowel(npc.getFlair().getWholeItem()[0]):
            textToReturn += ", and an "
        else:
            textToReturn += ", and a "
        textToReturn += npc.getFlair().getWholeItem()     

        return textToReturn

    def questionCharacter(self, npc):
        self.appendToNotes({npc: npc.getHintToGive()})

    def isVowel(self, character):
        match character:
            case 'a':
                return True
            case 'e':
                return True
            case 'i':
                return True
            case 'o':
                return True
            case 'u':
                return True
            case _:
                return False
