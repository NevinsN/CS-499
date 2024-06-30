# -*- coding: utf-8 -*-
from pymongo import MongoClient

class DBAccess(object):
    """ CRUD operations for Gothic Swine in MongoDB """

    def __init__(self, collection, adminLogin):
        # Initializing the MongoClient. This is hardwired to access the database
        # from within any game client. In future updates, a proper authorizaiton
        # system for unique user access might be implemented.
        #
        # The game system can only read databases in the GothicSwineDB
        # database
        
        #
        # Connection Variables
        #
        DB = "GothicSwineAssets"
        COL = collection
        #
        # Initialize Connection
        #
        if adminLogin:
            self.cluster = MongoClient("mongodb+srv://TGNiklaus:H00p3rman@gothicswinedb.xogt6d5.mongodb.net/?retryWrites=true&w=majority&appName=GothicSwineDB")
        else:
            self.cluster = MongoClient("mongodb+srv://playerClient:SlMK9ptcZJcn34oc@gothicswinedb.xogt6d5.mongodb.net/?retryWrites=true&w=majority&appName=GothicSwineDB")
        self.database = self.cluster[DB]
        self.collection = self.database[COL]
        #print("MongoDB database connected")

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data: 
            self.collection.insert_one(data)  # data should be dictionary            
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data:
            result = self.collection.find(data)
            return list(result)
        else:
            result = self.collection.find({})
            return list(result)
            
    # Create method to implement the U in CRUD
    def update(self, data, updateData):
        if data and updateData:
            result = self.collection.update_many(data, {"$set": updateData})
            return result
        else:
            return set()
            
    # Create method to implement the D in CRUD
    def delete(self, data):
        if data:
            result = self.collection.delete_many(data)
            return result
        else:
            return set()
        
    def getRandomSamplingOfValue(self, data):
        if data:
            result = self.collection.aggregate(data)
            return list(result)
        else:
            result = self.collection.find({})
            return list(result)
        
    def closeConnection(self):
        self.cluster.close()

    