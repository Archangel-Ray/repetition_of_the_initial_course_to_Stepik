# A list of cities is entered in one line separated by a space. You need to create an iterator for this list and
# use the iterator to display the first two values ​​(names of cities) in a column.

cities = iter(input('enter the names of several cities: ').split())
print(next(cities))
print(next(cities))
