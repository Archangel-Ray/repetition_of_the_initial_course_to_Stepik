# In some country banknotes are used in denominations of 1, 2, 4, 8, 16, 32 and 64. A natural number n is entered.
# How can the sum n be paid with the least amount of such banknotes? Display a list of banknotes to form the sum n
# (in one line separated by a space, starting with the largest and ending with the smallest).
# It is assumed that there is a sufficiently large number of banknotes of all denominations.

num = int(input('what salary do you want? '))

while num != 0:
    if num >= 64:
        num -= 64
        print(64, end=' ')
    elif num >= 32:
        num -= 32
        print(32, end=' ')
    elif num >= 16:
        num -= 16
        print(16, end=' ')
    elif num >= 8:
        num -= 8
        print(8, end=' ')
    elif num >= 4:
        num -= 4
        print(4, end=' ')
    elif num >= 2:
        num -= 2
        print(2, end=' ')
    elif num >= 1:
        num -= 1
        print(1, end=' ')
