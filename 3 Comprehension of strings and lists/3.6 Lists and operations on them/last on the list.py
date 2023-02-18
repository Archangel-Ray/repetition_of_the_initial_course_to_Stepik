# The names of cities are entered in one line separated by a space.
# Based on this line, a list is formed using the command:
#
# cities = input().split()
#
# It is necessary to display the value of the last element of
# this list on the screen.

cities = input('list some cities: ').split()
print(cities[-1])