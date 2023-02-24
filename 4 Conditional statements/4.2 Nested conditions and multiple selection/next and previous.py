# The date of a certain day is characterized by two natural
# numbers: m (serial number of the month) and n (number).
# According to the entered m and n (in one line separated by a space), determine:
#
# a) the date of the previous day (assume that m and n do not characterize January 1);
# b) the date of the next day (assume that m and n do not characterize December 31).
#
# The problem is to accept that the year is not a leap year.
# Print the previous date and the next date (in the format: mm.dd, where m is the day
# of the month; d is the number of the day) on one line separated by a space.
#
# P.S. Number of days in non-leap year months starting
# from January: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

month_numbers = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, n = list(map(int, input('enter the number of the month and the day of the month: ').split()))
if m == n == 1:
    print('12.31 01.02')
elif m == 12 and n == 31:
    print('12.30 01.01')
else:
    if n == 1:
        print(str(m-1).rjust(2, '0') + '.' + str(month_numbers[m-1]), end=' ')
    else:
        print(str(m).rjust(2, '0') + '.' + str(n-1).rjust(2, '0'), end=' ')
    if month_numbers[m] == n:
        print(str(m+1).rjust(2, '0') + '.01')
    else:
        print(str(m).rjust(2, '0') + '.' + str(n+1).rjust(2, '0'))
