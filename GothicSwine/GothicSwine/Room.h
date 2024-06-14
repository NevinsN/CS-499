#pragma once

#include <string>
#include <vector>
#include <map>

#include "NPC.h"

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * A class header to handle room creation
 *****************************************************************************************************/

class Room {
	int roomID;
	std::string roomName;
	std::string roomDescription;
	std::vector<NPC> charactersInRoom;
	std::map<int, Room> connectedRooms;

public:
	// Constructors and Destructors
	Room();  // default constructor
	Room(int roomCount); // overloaded constructor with just the roomCount to update ID
	Room(int roomID, std::string roomName, std::string roomDescription, int connectedFrom);  // overloaded constructor for roomID, roomName, roomDescription, and where it was connected from
	Room(int roomID, std::string roomName, std::string roomDescription, int connectedFrom, std::vector<NPC> charactersInRoom, std::map<int, Room> connectedRooms); // overloaded constructor for full manual room
	~Room();  // destructor

	// Setters and Getters
	int getRoomID();
	void setRoomName(std::string roomName);
	std::string getRoomName();
	void setRoomDescription(std::string roomDescription);
	std::string getRoomDescription();
	std::vector<NPC> getCharactersInRoom();
	NPC getCharacterByIndex(int index);
	void setConnectedRoomsByIndex(int index, Room roomToAdd);
	std::map<int, Room> getConnectedRooms();
	Room getConnectedRoomByIndex(int index);

	// Supporting Functions
	void addCharactersInRoom(NPC characterToAdd);
	void removeCharacterFromRoom(NPC characterToRemove);
	void generateRoomConnections(int roomsInList);  // randomly determines how many rooms are connected and fills them with placeholders
	void printRoomConnections(); // Test method
};