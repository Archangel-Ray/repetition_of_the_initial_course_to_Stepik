# An integer k is entered (1 = k = 365). Determine which day of the week
# (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday)
# is the k-th day of a non-leap year in which January 1 is Monday.

n = int(input('enter a number from 1 to 365: '))

if n % 7 == 1:
    print('Monday')
elif n % 7 == 2:
    print('Tuesday')
elif n % 7 == 3:
    print('Wednesday')
elif n % 7 == 4:
    print('Thursday')
elif n % 7 == 5:
    print('Friday')
elif n % 7 == 6:
    print('Saturday')
elif n % 7 == 0:
    print('Sunday')
