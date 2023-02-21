# The student grades (numbers from 2 to 5) are entered in one
# line separated by a space. It is necessary to determine the
# number of twos and display this value on the screen.

lst = list(map(int, input('Enter multiple ratings: ').split()))
print(lst.count(2))
