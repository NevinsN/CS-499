#pragma once

#include <string>

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 * 
 * An abstract character class to serve as a parent to other character types 
 *****************************************************************************************************/

class Char {
protected:
	int location = -1; // character location (-1 = no location)
	std::string characterName; 

public:
	// Constructor and Destructor
	Char() { this->characterName = "Nick"; } // Standard constructor setting character name
	~Char() {} // destructor

	// Setters and Getters
	void setLocation(int location) { this->location = location; }
	int getLocation() { return this->location; }
	void setCharacterName(std::string characterName) { this->characterName = characterName;  }
	std::string getCharacterName() { return this->characterName;  }
};
