# The names of cities are entered in a line separated by a space. It is necessary to form a list using list
# comprehension, containing names longer than five characters. Output the result in a line separated by a space.

print(*[city for city in input('several city names: ').split() if len(city) > 5])
