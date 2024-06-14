#include "ChangeDate.h"
#include <iostream>
#include <ctime>

ChangeDate::ChangeDate() {
	setCurrentDateStruct();
	this->newDateStruct = getCurrentDateStruct();
}

void ChangeDate::setCurrentDateStruct() {
	// get current date
	time_t now = time(0);

	localtime_s(currentDateStruct, &now);
	//this->currentDateStruct.tm_year += 1900;
	this->currentDateStruct->tm_mon += 1;
}

tm *ChangeDate::getCurrentDateStruct() {
	return this->currentDateStruct;
}

void ChangeDate::setNewDateStruct(int numDaysOffset) {
	tm *workingDateStruct = getCurrentDateStruct();
	tm* returnDate = getCurrentDateStruct();


	time_t workDateStructSeconds = mktime(workingDateStruct);

	workDateStructSeconds += 60 * 60 * 24 * numDaysOffset;

	std::cout << workDateStructSeconds << std::endl;

	localtime_s(returnDate, &workDateStructSeconds);

	/*int monthEnds[12] = {30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

	if (leapYearCheck(workingDateStruct.tm_year) == true) {
		monthEnds[1] = 29;
	}

	int modifier;

	if (numDaysOffset < 0) { modifier = -1; }
	else { modifier = 1; }

	workingDateStruct.tm_mday += numDaysOffset;

	while (workingDateStruct.tm_mday < 1 || workingDateStruct.tm_mday > monthEnds[workingDateStruct.tm_mon - 1]) {
		if (modifier == -1) {
			std::cout << workingDateStruct.tm_mon << std::endl;
			workingDateStruct.tm_mday += monthEnds[workingDateStruct.tm_mon - 1];
		}
		else {
			workingDateStruct.tm_mday -= monthEnds[workingDateStruct.tm_mon - 1];
		}
		workingDateStruct.tm_mon += modifier;

		if (workingDateStruct.tm_mon < 1) {
			workingDateStruct.tm_mon = 12;
			workingDateStruct.tm_year += modifier;
		}
		else if (workingDateStruct.tm_mon > 12) {
			workingDateStruct.tm_mon = 1;
			workingDateStruct.tm_year += modifier;
		}

		if (leapYearCheck(workingDateStruct.tm_year) == true) {
			monthEnds[1] = 29;
		}
		else { monthEnds[1] = 28; }*/

	std::cout << returnDate->tm_mon << " | " << returnDate->tm_mday << std::endl;
	

	this->newDateStruct = returnDate;
}

void ChangeDate::setNewDateStruct(tm startingDate, int numDaysOffset) {
	tm workingDateStruct = startingDate;

	int monthEnds[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

	workingDateStruct.tm_year += 1900;

	int modifier;

	if (numDaysOffset < 0) { modifier = -1; }
	else { modifier = 1; }

	workingDateStruct.tm_mday += numDaysOffset;

	//this->newDateStruct = workingDateStruct;
}

tm *ChangeDate::getNewDateStruct() {
	return this->newDateStruct;
}

bool ChangeDate::leapYearCheck(int year) {
	if (year % 100 == 0) {
		if (year % 400 == 0) {
			return true;
		}
		else {
			return false;
		}
	}
	else if (year % 4 == 0) {
		return true;
	}
	else {
		return false;
	}
}

std::string ChangeDate::getMonthStringFromInt(int month, int threeLetter) {
	switch (month) {
	case 1:
		if (threeLetter == 0) { return "January"; }
		else { return "Jan"; }
		break;
	case 2:
		if (threeLetter == 0) { return "February"; }
		else { return "Feb"; }
		break;
	case 3:
		if (threeLetter == 0) { return "March"; }
		else { return "Mar"; }
		break;
	case 4:
		if (threeLetter == 0) { return "April"; }
		else { return "Apr"; }
		break;
	case 5:
		return "May";
		break;
	case 6:
		if (threeLetter == 0) { return "June"; }
		else { return "Jun"; }
		break;
	case 7:
		if (threeLetter == 0) { return "July"; }
		else { return "Jul"; }
		break;
	case 8:
		if (threeLetter == 0) { return "August"; }
		else { return "Aug"; }
		break;
	case 9:
		if (threeLetter == 0) { return "September"; }
		else { return "Sept"; }
		break;
	case 10:
		if (threeLetter == 0) { return "October"; }
		else { return "Oct"; }
		break;
	case 11:
		if (threeLetter == 0) { return "November"; }
		else { return "Nov"; }
		break;
	case 12:
		if (threeLetter == 0) { return "December"; }
		else { return "Dec"; }
		break;
	}
}