#include "Room.h"

#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <map>

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * Class definitions to handle Room creation
 *****************************************************************************************************/

 /******************************************************************************************
   * Default constructor
   *****************************************************************************************/
Room::Room() {
	this->roomID = 0;
	this->roomName = "Foyer";
	this->roomDescription = "a painting of a laughing pig in Victorian clothing looking up, titled \"The Fool\"";
}

/******************************************************************************************
  * Overloaded constructor with just the roomCount to update ID
  *****************************************************************************************/
Room::Room(int roomCount) {
	this->roomID = roomCount;
	this->roomName = "roomName";
	this->roomDescription = "roomDescription";

}

/******************************************************************************************
  * Overloaded constructor for roomID, roomName, roomDescription, where connected from
  *****************************************************************************************/
Room::Room(int roomID, std::string roomName, std::string roomDescription, int connectedFrom) {
	this->roomID = roomID;
	this->roomName = roomName;
	this->roomDescription = roomDescription;
	generateRoomConnections(roomID);
}

/******************************************************************************************
  * Overloaded constructor for full manual room
  *****************************************************************************************/
Room::Room(int roomID, std::string roomName, std::string roomDescription, int connectedFrom, std::vector<NPC> charactersInRoom, std::map< int, Room> connectedRooms) {
	this->roomID = roomID;
	this->roomName = roomName;
	this->roomDescription = roomDescription;
	generateRoomConnections(roomID);
	this->charactersInRoom = charactersInRoom;
	this->connectedRooms = connectedRooms;
}

/******************************************************************************************
  * Destructor
  *****************************************************************************************/
Room::~Room() {}

/******************************************************************************************
  * Getter for roomID
  *****************************************************************************************/
int Room::getRoomID() { return this->roomID;  }

/******************************************************************************************
  * Setter for roomName
  *****************************************************************************************/
void Room::setRoomName(std::string roomName) { this->roomName = roomName; }

/******************************************************************************************
  * Getter for roomName
  *****************************************************************************************/
std::string Room::getRoomName() { return this->roomName;  }

/******************************************************************************************
  * Setter for roomDescription
  *****************************************************************************************/
void Room::setRoomDescription(std::string roomDescription) { this->roomDescription = roomDescription;  }

/******************************************************************************************
  * Getter for roomDescription
  *****************************************************************************************/
std::string Room::getRoomDescription() { return this->roomDescription;  }

/******************************************************************************************
  * Method to add a character into a room
  *****************************************************************************************/
void Room::addCharactersInRoom(NPC characterToAdd) { 
	this->charactersInRoom.push_back(characterToAdd);
}

/******************************************************************************************
  * Method to remove a character from the room
  *****************************************************************************************/
void Room::removeCharacterFromRoom(NPC characterToRemove) {
	std::vector<NPC>::iterator i = this->charactersInRoom.begin();

	for (auto& character : this->charactersInRoom) {
		if (character.getCharacterName() == characterToRemove.getCharacterName()) {
			this->charactersInRoom.erase(i);
		}
		i++;
	}
}

/******************************************************************************************
  * Getter for charactersInRoom
  *****************************************************************************************/
std::vector<NPC> Room::getCharactersInRoom() {
	return this->charactersInRoom;
}

/******************************************************************************************
  * Method to return a single character in the room by index
  *****************************************************************************************/
NPC Room::getCharacterByIndex(int index) {
	return this->charactersInRoom[index];
}

/******************************************************************************************
  * Method to add a room to a connection point in current room
  *****************************************************************************************/
void Room::setConnectedRoomsByIndex(int index, Room roomToAdd) {
	// Checks to see if the index exists. 
	// Index is set upon initialization with a placeholder. 
	// If Index doesn't exist, then that room does not have a connection at that index
	if (this->connectedRooms.find(index) != this->connectedRooms.end()) {
		this->connectedRooms[index] = roomToAdd;  // Add room to conneciton index
	}
	else {
		std::cout << "no room in that direction" << std::endl;
	}
}

/******************************************************************************************
  * Getter for connectedRooms
  *****************************************************************************************/
std::map<int, Room> Room::getConnectedRooms() {
	return this->connectedRooms;
}

/******************************************************************************************
  * Getter for single connected room by index
  *****************************************************************************************/
Room Room::getConnectedRoomByIndex(int index) {
	return this->connectedRooms[index];
}

/******************************************************************************************
  * Method to randomly determine how many rooms are connected and fill with placeholders
  *****************************************************************************************/
void Room::generateRoomConnections(int roomsInList) {
	// for loop to go through all possible connection points.
	// NOTE: this could be more modular, but 4 is what works for this program at the moment
	for (int i = 0; i < getConnectedRooms().size(); i++) {
		if (rand() % 2 == 0) {  // essentially a coin flip. If the random number is even, a room is added to index point
			this->connectedRooms[i] = (Room(roomsInList));
		}
	}
}

/******************************************************************************************
  * Method for test prints. Will be removed once finished
  *****************************************************************************************/
void Room::printRoomConnections() {
	for (auto index : this->connectedRooms) {
		std::cout << index.second.getRoomName() << std::endl;
	}
}