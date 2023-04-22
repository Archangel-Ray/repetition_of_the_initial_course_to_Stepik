# The input to the program is a decimal integer. Using bitwise operations, check if the 5th or 1st bit of the entered
# number is on. If at least one of these bits is on, then print the word YES, otherwise - the word NO.

x = int(input())
if x & 34 == 32 or x & 2 == 2:
    print('YES')
else:
    print('NO')
