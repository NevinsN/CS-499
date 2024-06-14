#pragma once
#ifndef CHANGEDATE
#define CHANGEDATE

#include <ctime>
#include <string>

class ChangeDate {
	struct tm *currentDateStruct;
	struct tm *newDateStruct;

public:
	ChangeDate();
	void setCurrentDateStruct();
	tm *getCurrentDateStruct();
	void setNewDateStruct(int numDaysOffset);
	void setNewDateStruct(tm startingDate, int numDaysOffset);
	tm *getNewDateStruct();
	bool leapYearCheck(int year);
	std::string getMonthStringFromInt(int month, int threeLetter);
};


#endif 