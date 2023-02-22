# A matrix of numbers of three rows is entered. In each line,
# the numbers are separated by a space. It is necessary to display
# the last column of this matrix as a string of three numbers
# separated by a space.

matrix = [list(map(int, input('write four numbers: ').split())), list(map(int, input('still write four numbers: ').split())), list(map(int, input('still write four numbers: ').split()))]
print(matrix[0][-1], matrix[1][-1], matrix[2][-1])