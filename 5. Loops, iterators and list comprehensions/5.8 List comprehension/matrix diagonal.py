# A natural number N is introduced. Using list comprehension, form a two-dimensional list of size N x N, consisting
# of zeros and ones along the main diagonal. (The main diagonal is the elements that run diagonally from the upper
# left corner of the matrix to its lower right corner).
# Output the result in the form of a table of numbers as shown in the example below.

n = int(input('digit: '))
matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
for i in matrix:
    print(*i, sep=' ')
