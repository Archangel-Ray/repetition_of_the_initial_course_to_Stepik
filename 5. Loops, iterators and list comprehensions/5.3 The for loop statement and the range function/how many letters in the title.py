# The names of cities are entered in one line separated by a space. You need to convert the input to a list.
# Then, iterate over it with a for loop and replace the element values ​​with the length of the name of the
# corresponding city. The result is displayed on the screen as a sequence of numbers separated by a space in one line.

for i in input('do you know many cities? ').split():
    print(len(i), end=' ')
