#pragma once

#include <string>

#include "Char.h"
#include "Item.h"

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * A class header to handle NPCs
 *****************************************************************************************************/

class NPC : public Char {
	Item apparel;   // houses apparel item with color, design, and type
	Item accessory; // houses accessory item with color, design, and type
	Item flair;     // houses flair item with color, design, and type

public:
	// Constructors and Destructors
	NPC(); // default constructor
	NPC(std::string npcName);  // constructor overloaded with name
	~NPC(); // destructor
	
	// Setters and Getters
	void setApparel(Item item);
	Item getApparel();
	void setAccessory(Item item);
	Item getAccessory();
	void setFlair(Item item);
	Item getFlair();
};
