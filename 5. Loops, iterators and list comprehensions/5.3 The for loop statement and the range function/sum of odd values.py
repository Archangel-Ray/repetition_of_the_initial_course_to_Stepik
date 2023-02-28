# Integer numbers are entered in one line separated by a space. You need to convert this data to a list of integers.
# Then, iterate over this list in a for loop and sum up all the odd values. Display the result on the screen.

s = 0
for i in map(int, input('enter some numbers: ').split()):
    if i % 2 != 0:
        s += i
print(s)
