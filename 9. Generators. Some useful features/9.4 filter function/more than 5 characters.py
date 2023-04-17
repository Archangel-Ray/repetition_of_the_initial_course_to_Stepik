# The names of cities are entered in one line separated by a space. It is necessary to define a filter function that
# would return only names longer than 5 characters. Extract the first three received values ​​using the next function
# and display them on the screen in one line separated by a space.
# (It is assumed that at least three values ​​are present).

s = filter(lambda x: len(x) > 5, input("enter some city names: ").split())
print(next(s), end=' ')
print(next(s), end=' ')
print(next(s))
