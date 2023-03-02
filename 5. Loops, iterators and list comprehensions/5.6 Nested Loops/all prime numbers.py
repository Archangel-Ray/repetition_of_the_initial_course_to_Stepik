# A natural number n is entered. It is necessary to find all prime numbers that are less than this number n, that is,
# in the range [2; n]. Output the result to the screen in a line separated by a space.

for i in range(2, int(input('natural number: '))):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, end=' ')
