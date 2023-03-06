# Enter a list of integers in one line separated by a space. Use a dictionary to extract only unique (non-repeating)
# input values ​​and then form a list of unique numbers.
# Display it on the screen as a set of numbers separated by a space.
#
# P.S. Such a task is usually solved through sets, but we have not yet gone through them, so we will use a dictionary.

string = input('write some numbers: ').split()
d = dict.fromkeys(string)
print(*d.keys())
