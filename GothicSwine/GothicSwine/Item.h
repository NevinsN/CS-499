#pragma once

#include <cstdlib>

#include <string>
#include <vector>

/******************************************************************************************************
 * Author: Nicholas Nevins
 * Last Update: 5-30-24
 *
 * A class header to handle creation of items 
 *****************************************************************************************************/

class Item {
	int itemID;
	std::string type; // notes what type of an item it is (Apparel, Flair, Accessory)
	std::string color;
	std::string design;
	std::string baseItem; 

	std::vector<std::string> colorVec;
	std::vector<std::string> designVec;
	std::vector<std::string> baseItemVec;
	

public:
	// Constructors and Destructor
	Item();
	Item(int itemID, std::string type, std::string color, std::string design, std::string baseItem);
	Item(int itemID,  std::string type, std::string color, std::string design, std::string baseItem,
		std::vector<std::string> colorVec, std::vector<std::string> designVec, std::vector<std::string> baseItemVec);
	~Item();
	
	// Setters and Getters
	int getItemID();
	void setType(std::string type);
	std::string getType();
	void setColor(std::string color);
	std::string getColor();
	void setDesign(std::string design);
	std::string getDesign();
	void setBaseItem(std::string baseItem);
	std::string getBaseItem();
	void setColorVec(std::vector<std::string> colorVec);
	std::vector<std::string> getColorVec();
	void setDesignVec(std::vector<std::string> designVec);
	std::vector<std::string> getDesignVec();
	void setBaseItemVec(std::vector<std::string> baseItemVec);
	std::vector<std::string> getBaseItemVec();

	// Method to return full item string
	std::string getFullItemDescription();

	// Supporting Methods
	std::string assignRandomVectorElements();
};