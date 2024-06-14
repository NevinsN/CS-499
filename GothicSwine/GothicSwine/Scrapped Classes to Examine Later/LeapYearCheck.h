


bool leapYearCheck(int year) {
	if (year % 100 == 0) {
		if (year % 400 == 0) {
			return true;
		}
		else if (year % 4 == 0) {
			return true;
		}
		else {
			return false;
		}
	}

	return false;
}
