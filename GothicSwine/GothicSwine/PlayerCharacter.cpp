#include "PlayerCharacter.h"

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * Class definitions to handle PlayerCharacters
 *****************************************************************************************************/

/******************************************************************************************
 * Default Constructor setting character to location 0 (Foyer)
 *****************************************************************************************/
PlayerCharacter::PlayerCharacter() {
	setLocation(0);
}

/******************************************************************************************
 * Adds clue to the cluesGathered
 *****************************************************************************************/
void PlayerCharacter::addClueToVector(std::string clue) { this->cluesGathered.push_back(clue); }

/******************************************************************************************
 * Getter for cluesGathered
 *****************************************************************************************/
std::vector<std::string> PlayerCharacter::getCluesGathered() { return this->cluesGathered; }

/******************************************************************************************
 * Getter for single element of cluesGathered by index
 *****************************************************************************************/
std::string PlayerCharacter::getClueByIndex(int index) { return this->cluesGathered[index]; }