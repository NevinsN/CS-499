#include "NPC.h"

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * Class definitions to handle NPCs
 *****************************************************************************************************/

 /******************************************************************************************
  * Default constructor set to Nick
  *****************************************************************************************/
NPC::NPC() {
	setCharacterName("Nick");
}

/******************************************************************************************
  * Overloaded constructor for custom NPC name
  *****************************************************************************************/
NPC::NPC(std::string characterName) {
	setCharacterName(characterName);
}

/******************************************************************************************
  * Destructor
  *****************************************************************************************/
NPC::~NPC() {}

/******************************************************************************************
  * Setter for the apparel item. Requires a color, material, and type
  *****************************************************************************************/
void NPC::setApparel(Item item) {
	this->apparel = item;
}

/******************************************************************************************
  * Getter for the apparel item.
  *****************************************************************************************/
Item NPC::getApparel() { return this->apparel; }

/******************************************************************************************
  * Setter for the accessory item. Requires a color, material, and type
  *****************************************************************************************/
void NPC::setAccessory(Item item) {
	this->accessory = item;
}

/******************************************************************************************
  * Getter for the accessory item.
  *****************************************************************************************/
Item NPC::getAccessory() { return this->accessory; }

/******************************************************************************************
  * Setter for the apparel item. Requires a color, material, and type
  *****************************************************************************************/
void NPC::setFlair(Item item) {
	this->flair = item;
}

/******************************************************************************************
  * Getter for the apparel item. 
  *****************************************************************************************/
Item NPC::getFlair() { return this->flair; }