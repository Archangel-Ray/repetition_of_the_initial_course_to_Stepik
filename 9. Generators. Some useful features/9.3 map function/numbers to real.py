# The input is a list of real numbers written in a string separated by a space. Use the map function to convert
# the numbers in a string to their real representation and display the first three numbers.
# (It is assumed that there are at least three real numbers). Implement the extraction of numbers through
# the next function. Display the result in a string separated by a space.

n = map(float, input("enter real numbers: ").split())
print(next(n), end=' ')
print(next(n), end=' ')
print(next(n))
