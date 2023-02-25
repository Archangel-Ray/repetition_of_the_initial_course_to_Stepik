# Enter the cost of one book x dollars (real number). It is necessary to display on the screen the cost of 2, 3, ... 10
# such books separated by a space, accurate to tenths. Implement the program with a while loop.

cost = float(input('how much does the book cost? '))
count = 2
while count < 11:
    print(round((cost * count), 1), end=' ')
    count += 1
