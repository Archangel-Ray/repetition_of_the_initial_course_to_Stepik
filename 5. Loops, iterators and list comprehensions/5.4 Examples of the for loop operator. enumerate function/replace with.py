# The list is entered in the form of real numbers in one line separated by a space. First, you need to form a list from
# the entered string. Then, all negative values ​​in this list are replaced by -1.0. The result is displayed on the
# screen as a string of numbers separated by a space. The program should be implemented using the enumerate function.

string = list(map(float, input('enter some real numbers: ').split()))
for i, n in enumerate(string):
    if n < 0:
        string[i] = -1.0

print(*string)
