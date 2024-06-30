import pandas as pd

import Database.DBAccess as DBAccess

class CreateDBItems(object):
    _df = pd.DataFrame()
    _Categories = []

    def __init__(self, dataCSV):
        self._df = pd.read_csv(dataCSV)
        self._Categories = self._df.columns.values

        self.buildDBEntries()

    def buildDBSchema(self, type, color, design, baseItem):
        query = {
            "type": type,
            "color": color,
            "design": design,
            "baseItem": baseItem
        }

        return query
    
    def buildDBEntries(self):
        db = DBAccess.DBAccess("Items", True)

        db.delete({})

        accessoryList = self.buildSchemasForType("accessory")
        apparelList = self.buildSchemasForType("apparel")
        flairList = self.buildSchemasForType("flair")

        for x in accessoryList:
            db.create(x)

        for x in apparelList:
            db.create(x)

        for x in flairList:
            db.create(x)

        print("DB Loading finished")
        db.closeConnection()

    def buildSchemasForType(self, type):
        outputList = []

        baseItemInit = self._df.loc[:, type]
        colorInit = self._df.loc[:, "color"]
        designInit = self._df.loc[:, "design"]

        for x in baseItemInit:
            if pd.isna(x):
                continue
            else:
                for y in colorInit:
                    if pd.isna(y):
                        continue
                    else:
                        for z in designInit:
                            if pd.isna(z):
                                continue
                            else:
                                outputList.append(self.buildDBSchema(type, y, z, x))

        return outputList