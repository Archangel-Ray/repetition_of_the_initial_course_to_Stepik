# Enter the serial number of the month (1, 2, ..., 12).
# Display the number of days in this month. Assume that the year is not a leap year.
# Implement through a conditional statement, in which no more
# than three branches (blocks) should be used.
#
# P.S. Number of days in non-leap year months starting
# from January: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

month = int(input('enter month number: '))

if month in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif month == 2:
    print(28)
elif month in (4, 6, 9, 11):
    print(30)
