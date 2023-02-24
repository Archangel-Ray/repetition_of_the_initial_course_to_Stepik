# An integer k is entered (1 = k = 365). Determine which day of the week
# (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday)
# is the k-th day of a non-leap year in which January 1 is Monday.


print(['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][int(input('enter a number from 1 to 365: '))%7])
