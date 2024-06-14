#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <cstring>
#include <cstdlib>

#include "MapManager.h"

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * Class definitions to handle the MapManager
 *****************************************************************************************************/

 /******************************************************************************************
   * Default constructor
   *****************************************************************************************/
MapManager::MapManager() {
	parseRoomFile("roomDetails.txt");
}

/******************************************************************************************
  * Default constructor with parameter for number of rooms and the file to parse
  *****************************************************************************************/
MapManager::MapManager(int numRooms, std::string roomFile) {
	parseRoomFile(roomFile);
}

/******************************************************************************************
  * Destructor
  *****************************************************************************************/
MapManager::~MapManager() {}

/******************************************************************************************
  * Method to add a room to roomList vector via push_back
  *****************************************************************************************/
void MapManager::addRoomToVector(Room roomToAdd) {
	this->roomList.push_back(roomToAdd);
}

/******************************************************************************************
  * Method to remove a room from roomList
  *****************************************************************************************/
void MapManager::removeRoomFromVector(Room roomToRemove) {
	std::vector<Room>::iterator i = this->roomList.begin();  // iterate to erase

	// for loop goes through whole vector
	for (auto & room : this->roomList) {
		// if roomID is found
		if (room.getRoomID() == roomToRemove.getRoomID()) {
			this->roomList.erase(i); // erase
		}
		i++;
	}
}

/******************************************************************************************
  * Getter for individual rooms by roomID
  *****************************************************************************************/
Room MapManager::getRoomByID(int roomID) {
	return this->roomList[roomID];
}

/******************************************************************************************
  * Method to set roomDetails with desired roomStruct
  *****************************************************************************************/
void MapManager::addStructToRoomDetails(RoomStruct roomStruct) {
	this->roomDetails.push_back(roomStruct);
}

/******************************************************************************************
  * Getter for roomDetails
  *****************************************************************************************/
std::vector<MapManager::RoomStruct> MapManager::getRoomDetails() {
	return this->roomDetails;
}

/******************************************************************************************
  * Getter for single room's details by index
  * index = 0 will return name
  * index = 1 will return description
  *****************************************************************************************/
MapManager::RoomStruct MapManager::getRoomDetailsByIndex(int index) {
	return this->roomDetails[index];
}

/******************************************************************************************
  * Method to parse and store desired txt document
  *****************************************************************************************/
void MapManager::parseRoomFile(std::string roomFile) {
	std::string rawText;  // text string to hold initial file data
	char delim = '|';     // deliminator used to divide items in the txt file

	std::string text;     // string to store individual strings while parsing
	std::vector<std::string> parsedText;  // final vector for post parsed text

	std::ifstream roomFileStream(roomFile.c_str());  // read file into ifstream

	// verify the file opened properly
	if (!roomFileStream.is_open()) {
		std::cerr << "File did not open" << std::endl;
		return;
	}

	// copy ifstream into rawText
	while (getline(roomFileStream, rawText)) {
		std::cout << "text copied" << std::endl;
	}

	// close ifstream
	roomFileStream.close();

	// stringstream to parse by delimiter
	std::stringstream textToParse(rawText);

	// loops through textToParse and divides at the delimiter, stored in parseText as individual elements
	while (getline(textToParse, text, delim)) {
		parsedText.push_back(text);
	}

	// foor loop moves through parsedText, assigns elements to a new RoomStruct, pushes that to roomDetails
	// NOTE: loop increments by 2, as we add two elements at a time, one to name and one to description
	for (int i = 0; i < parsedText.size(); i += 2) {
		RoomStruct tempRoomStruct; 
		tempRoomStruct.setRoomName(parsedText[i]);
		tempRoomStruct.setRoomDescription(parsedText[i + 1]);
		addStructToRoomDetails(tempRoomStruct);
	}
}

/******************************************************************************************
  * Setters and Getters for roomStruct variables
  *****************************************************************************************/
void MapManager::RoomStruct::setRoomName(std::string roomName) {
	this->roomName = roomName;
}

std::string MapManager::RoomStruct::getRoomName() {
	return this->roomName;
}

void MapManager::RoomStruct::setRoomDescription(std::string roomDescription) {
	this->roomDescription = roomDescription;
}

std::string MapManager::RoomStruct::getRoomDescription() {
	return this->roomDescription;
}

/******************************************************************************************
  * Method to get the size of roomList. Used primarily to create incremental room IDs as
  * new rooms are created
  *****************************************************************************************/
int MapManager::getRoomListSize() {
	return size(this->roomList);
}

void MapManager::populateMap(int numRooms) {
	// FIXME: Create Function
}