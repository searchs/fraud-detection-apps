# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct ouptuts yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        day += 1
        return year, month, day
    else:
        if month == 12:
            year += 1
            return year, 1, 1
        else:
            month += 1
            return year, month, 1


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    daysDiff = 0
    if  year1 == year2:
        if month1 == month2:
            daysDiff =  day2 - day1
            return daysDiff
        else:
           
            diff_days = (30 - day1) + day2
            diff_months = month2 - month1
            daysDiff = diff_days + 30*(diff_months -1)
            return daysDiff
    elif year1 < year2:
        years_diff = year2 - year1
        months_diff =  (12 - month1) + month2
        diff_days = (30 - day1) + day2
        daysDiff = diff_days + 30*(months_diff -1)
        return daysDiff

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print args,"Test case passed!"

test()

