# Enter the serial number of the month (1, 2, ..., 12).
# Display the number of days in this month. Assume that the year is not a leap year.
# Implement through a conditional statement, in which no more
# than three branches (blocks) should be used.
#
# P.S. Number of days in non-leap year months starting
# from January: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

month = int(input('enter month number: '))

if month == 1:
    print(31)
elif month == 2:
    print(28)
elif month == 3:
    print(31)
elif month == 4:
    print(30)
elif month == 5:
    print(31)
elif month == 6:
    print(30)
elif month == 7:
    print(31)
elif month == 8:
    print(31)
elif month == 9:
    print(30)
elif month == 10:
    print(31)
elif month == 11:
    print(30)
elif month == 12:
    print(31)
