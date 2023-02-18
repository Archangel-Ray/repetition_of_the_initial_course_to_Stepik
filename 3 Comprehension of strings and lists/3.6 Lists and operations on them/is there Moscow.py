# The names of cities are entered in one line separated by a space.
# Based on this line, a list is formed using the command:
#
# cities = input().split()
#
# It is necessary to check if the city 'Moscow' is present
# in this list. Display True if present and False otherwise.
# Solve this problem without using the conditional operator.

cities = input('list some cities: ').split()
print("Moscow" in cities)
