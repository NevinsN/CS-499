#pragma once
#ifndef CHANGEDATETESTSHELL
#define CHANGEDATETESTSHELL

#include <ctime>
#include <iostream>

#include "ChangeDate.h"

class ChangeDateTestShell {
	ChangeDate cd;

public:
	ChangeDateTestShell() {
		
	}

	void runTest(int daysOffset) {
		tm *currTime = cd.getCurrentDateStruct();
		cd.setNewDateStruct(daysOffset);
		tm *newTime = cd.getNewDateStruct();

		//std::cout << cd.getMonthStringFromInt(currTime.tm_mon, 0) << " " << currTime.tm_mday << ", " << currTime.tm_year << std::endl;
		//std::cout << cd.getMonthStringFromInt(newTime.tm_mon, 0) << " " << newTime.tm_mday << ", " << newTime.tm_year << std::endl;

		std::cout << currTime->tm_mon << " " << currTime->tm_mday << ", " << currTime->tm_year << std::endl;
		std::cout << newTime->tm_mon << " " << newTime->tm_mday << ", " << newTime->tm_year << std::endl;
	}
};

#endif