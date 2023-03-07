# The names of cities are entered in one line separated by a space. Based on them, a tuple is formed.
# If this tuple does not contain the city 'Moscow', then it should be added to the end of the tuple.
# Output the result to the screen as a string with city names separated by a space.

cities = tuple(input('what cities do you know? ').split())
print(*(cities+('Moscow',) if 'Moscow' not in cities else cities))
