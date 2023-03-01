# The list is entered in the form of integers in one line separated by a space. You must first form a list based
# on the entered string, and then change each value of this list by squaring. Display the result on the screen as
# a string of received numbers separated by a space. The program should be implemented using the enumerate function.

string = list(map(int, input('enter some numbers: ').split()))

for i, n in enumerate(string):
    string[i] = n**2

print(*string)
