#pragma once

#include <vector>, <string>

#include "Char.h"

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * A class header to handle the player character
 *****************************************************************************************************/

class PlayerCharacter : public Char {
	std::vector<std::string> cluesGathered;

public:
	// Constructor
	PlayerCharacter();
	
	// Adds clue to cluesGathered
	void addClueToVector(std::string clue);
	
	// Getters for cluesGathered
	std::vector<std::string> getCluesGathered();
	std::string getClueByIndex(int index);
};