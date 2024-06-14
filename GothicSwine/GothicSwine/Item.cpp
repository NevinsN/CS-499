#include <cstdlib>

#include "Item.h"

/******************************************************************************************
 * Default constructor
 *****************************************************************************************/
Item::Item() {
	this->itemID = 0;
	this->type = "apparel";
	this->color = "red";
	this->design = "houndstooth";
	this->baseItem = "shirt";
}

/******************************************************************************************
 * Constructor with a provided type, color, design, and baseItem
 *****************************************************************************************/
Item::Item(int itemID, std::string type, std::string color, std::string design, std::string baseItem) {
	this->itemID = itemID;
	this->type = type;
	this->color = color;
	this->design = design;
	this->baseItem = baseItem;
}

/******************************************************************************************
 * Constructor with a provided type, color, design, baseItem,
 * colorVev, designVec, and baseItemVec
 *****************************************************************************************/
Item::Item(int itemID, std::string type, std::string color, std::string design, std::string baseItem,
	std::vector<std::string> colorVec, std::vector<std::string> designVec, std::vector<std::string> baseItemVec) {
	this->itemID = itemID;
	this->type = type;
	this->color = color;
	this->design = design;
	this->baseItem = baseItem;
	this->colorVec = colorVec;
	this->designVec = designVec;
	this->baseItemVec = baseItemVec;
}

/******************************************************************************************
 * Destructor
 *****************************************************************************************/
Item::~Item() {}

int Item::getItemID() { return this->itemID; }

/******************************************************************************************
 * Setter for type
 *****************************************************************************************/
void Item::setType(std::string type) { this->type = type; }

/******************************************************************************************
 * Getter for type
 *****************************************************************************************/
std::string Item::getType() { return this->type; }

/******************************************************************************************
 * Setter for color
 *****************************************************************************************/
void Item::setColor(std::string color) { this->color = color; }

/******************************************************************************************
 * Getter for color
 *****************************************************************************************/
std::string Item::getColor() { return this->color; }

/******************************************************************************************
 * Setter for design
 *****************************************************************************************/
void Item::setDesign(std::string design) { this->design = design; }

/******************************************************************************************
 * Getter for design
 *****************************************************************************************/
std::string Item::getDesign() { return this->design; }

/******************************************************************************************
 * Setter for baseItem
 *****************************************************************************************/
void Item::setBaseItem(std::string baseItem) { this->baseItem = baseItem; }

/******************************************************************************************
 * Getter for baseItem
 *****************************************************************************************/
std::string Item::getBaseItem() { return this->baseItem; }

/******************************************************************************************
 * Setter for colorVec
 *****************************************************************************************/
void Item::setColorVec(std::vector<std::string> colorVec) { this->colorVec = colorVec; }

/******************************************************************************************
 * Getter for colorVec
 *****************************************************************************************/
std::vector<std::string> Item::getColorVec() { return this->colorVec; }

/******************************************************************************************
 * Setter for designVec
 *****************************************************************************************/
void Item::setDesignVec(std::vector<std::string> designVec) { this->designVec = designVec; }

/******************************************************************************************
 * Getter for designVec
 *****************************************************************************************/
std::vector<std::string> Item::getDesignVec() { return this->designVec; }

/******************************************************************************************
 * Setter for baseItemVec
 *****************************************************************************************/
void Item::setBaseItemVec(std::vector<std::string> baseItemVec) { this->baseItemVec = baseItemVec; }

/******************************************************************************************
 * Getter for baseItemVec
 *****************************************************************************************/
std::vector<std::string> Item::getBaseItemVec() { return this->baseItemVec; }

/******************************************************************************************
 * Getter for the full item description
 *****************************************************************************************/
std::string Item::getFullItemDescription() {
	return getColor() + " " + getDesign() + " " + getBaseItem();
}

/******************************************************************************************
 * Assigns color, design, and baseItem randomly
 *****************************************************************************************/
std::string Item::assignRandomVectorElements() {
	setColor(getColorVec()[rand() % getColorVec().size()]);
	setDesign(getDesignVec()[rand() % getDesignVec().size()]);
	setBaseItem(getBaseItemVec()[rand() % getBaseItemVec().size()]);
}