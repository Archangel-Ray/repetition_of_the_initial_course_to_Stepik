# The input to the program is a decimal integer. Using bitwise operations, check if the 6th and 3rd bits of the entered
# number are included. If both of them are enabled, then print the word YES, otherwise - the word NO.

x = bin(int(input()))
if x[-7] == '1' and x[-4] == '1':
    print('YES')
else:
    print('NO')
