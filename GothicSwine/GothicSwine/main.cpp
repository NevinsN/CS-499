/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * This file will handle instantiating the pieces that make up the game 
 * for interaction with the rest of the system
 *****************************************************************************************************/

#include <iostream>
#include <cstdlib>

#include "NPC.h"
#include "Room.h"
#include "MapManager.h"
#include "Item.h"



int main()
{
	std::srand(time(0));

	NPC npc;
	MapManager RM = MapManager(4, std::string("roomDetails.txt"));

	RM.addRoomToVector(Room(RM.getRoomListSize()));

	std::cout << "done" << std::endl;

	Room room = RM.getRoomByID(0);

	npc.setCharacterName("Joe");
	std::cout << npc.getCharacterName() << std::endl;
	std::cout << std::endl << room.getRoomID() << " | " << room.getRoomName() << " | " << room.getRoomDescription() << std::endl;

	room.setRoomDescription("A cool room");
	room.setRoomName("Cool Room");

	std::cout << std::endl << room.getRoomID() << " | " << room.getRoomName() << " | " << room.getRoomDescription() << std::endl;

	room.addCharactersInRoom(npc);

	int thing[] = {0, 1, 1, 0};

	Room room2(RM.getRoomListSize(), RM.getRoomDetailsByIndex(5).getRoomName(), RM.getRoomDetailsByIndex(5).getRoomDescription(), 0);

	RM.addRoomToVector(room2);

	std::cout << room2.getRoomID() << std::endl;

	for (int i = 0; i < 5; i++) {
		Room room = Room(RM.getRoomListSize());
		RM.addRoomToVector(room);
		std::cout << room.getRoomID() << std::endl;
	}

	room2.setConnectedRoomsByIndex(1, Room(RM.getRoomListSize(), RM.getRoomDetailsByIndex(3).getRoomName(), RM.getRoomDetailsByIndex(3).getRoomDescription(), 0));
	room2.printRoomConnections();
	std::cout << room2.getConnectedRoomByIndex(1).getRoomName() << " | " << room2.getConnectedRoomByIndex(1).getRoomDescription() << std::endl;
	
	std::cout << "room added" << std::endl;

	for (auto character : room.getCharactersInRoom()) {
		std::cout << character.getCharacterName() << std::endl;
	}

	for (auto room : room.getConnectedRooms()) {
		std::cout << room.second.getRoomName() << std::endl;
	}

	for (auto room : room.getConnectedRooms()) {
		std::cout << room.second.getRoomName() << std::endl;
	}

	std::cout << RM.getRoomDetailsByIndex(0).getRoomName() << " | " << RM.getRoomDetailsByIndex(3).getRoomName() << " | " << RM.getRoomDetailsByIndex(4).getRoomName() << std::endl;
}
