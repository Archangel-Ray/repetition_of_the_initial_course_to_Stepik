# A natural number N is entered. It is necessary to generate a nested list using list comprehension, size N x N,
# where the first line would contain all zeros, the second - all ones, the third - all twos, and so on up
# to the Nth line. Output the result in the form of a table of numbers as shown in the example below.

n = int(input('digit: '))
matrix = [[j for _ in range(n)] for j in range(n)]
for i in matrix:
    print(*i, sep=' ')
