# An arithmetic expression is written as a string, for example:
#
# '10 + 25 - 12'
# or
# '10 + 25 - 12 + 20 - 1 + 3'
#
# etc. That is, the number of actions can be different.
#
# It is necessary to perform the calculation and display the result on the screen.
# It is assumed that only addition (+) and subtraction (-) are used here as arithmetic operations,
# and non-negative integers are used as operands. Note that these operators can be written with or without spaces.

arithmetic_expression = input('write an example: ')
res = 0
num = ''
expression = ''
for i in arithmetic_expression:
    if i.isdigit():
        num += i
    elif i == ' ':
        continue
    elif i == '+' or i == '-':
        if expression == '':
            res += int(num)
            num = ''
            if i == '+':
                expression = '+'
            elif i == '-':
                expression = '-'
        elif expression == '+':
            res += int(num)
            num = ''
            if i == '+':
                expression = '+'
            elif i == '-':
                expression = '-'
        elif expression == '-':
            res -= int(num)
            num = ''
            if i == '+':
                expression = '+'
            elif i == '-':
                expression = '-'
if expression == '+':
    res += int(num)
elif expression == '-':
    res -= int(num)

print(res)
