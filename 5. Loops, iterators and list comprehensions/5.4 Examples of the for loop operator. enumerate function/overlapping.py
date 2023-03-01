# The list is entered in the form of integers in one line separated by a space. First, you need to generate a list
# from the input string. Then, each element of this list is duplicated once. The result is displayed on the screen
# as a string of received numbers, written with a space.

string = list(map(int, input('enter some numbers: ').split()))
for i in string:
    print(i, i, end=' ')
