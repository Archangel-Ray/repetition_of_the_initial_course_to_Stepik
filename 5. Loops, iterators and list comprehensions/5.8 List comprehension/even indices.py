# Enter a list of real numbers. Use the list comprehension to construct a list consisting of the elements of the given
# list that have even indices (that is, select all elements with even indices).
# The result is displayed on the screen in one line separated by a space.

print(*[num for i, num in enumerate(input('multiple real numbers: ').split()) if i % 2 == 0])
