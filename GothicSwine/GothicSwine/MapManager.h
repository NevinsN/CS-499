#pragma once

#include <vector>
#include <string>
#include <map>

#include "Room.h"

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * A class header to handle the Room Manager
 *****************************************************************************************************/

class MapManager {
	// RoomStruct is an efficient way to store and return name and description
	// Mostly used in parsing and returning the file
	struct RoomStruct {
	private:
		std::string roomName;
		std::string roomDescription;

	public:
		void setRoomName(std::string roomName);
		std::string getRoomName();
		void setRoomDescription(std::string roomDescription);
		std::string getRoomDescription();
	};

	std::vector<Room> roomList;           // list of all created rooms
	std::vector<RoomStruct> roomDetails;  // list of room data parsed from roomDetails.txt

public:
	// Constructors and Destructor
	MapManager();  // default constructor
	MapManager(int numRooms, std::string roomFile);  // overloaded constructor to set total rooms and the file to parse 
	~MapManager();

	// Supporting Methods
	void addRoomToVector(Room roomToAdd);
	void removeRoomFromVector(Room roomToRemove);
	Room getRoomByID(int roomID);
	void addStructToRoomDetails(RoomStruct roomStruct);
	std::vector<RoomStruct> getRoomDetails();
	RoomStruct getRoomDetailsByIndex(int index);
	void parseRoomFile(std::string roomFile);
	int getRoomListSize();

	void populateMap(int numRooms);
};