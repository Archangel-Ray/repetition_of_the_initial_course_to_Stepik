# A two-dimensional list of 5 x 5 elements is entered, consisting of integers (see below for an input example).
# Check if this two-dimensional list is symmetrical about the main diagonal.
# The main diagonal is the one that goes from the upper left corner of the two-dimensional array to the lower right.
# Display YES if the matrix is ​​symmetric and NO otherwise.
#
# P.S. To read the entire list, the program has already written the initial lines.

lst_in = [[2, 3, 4, 5, 6],
          [3, 2, 7, 8, 9],
          [4, 7, 2, 0, 4],
          [5, 8, 0, 2, 1],
          [6, 9, 4, 1, 2]
          ]

flag = 'YES'
for i in range(len(lst_in)):
    if flag == 'NO':
        break
    for j in range(len(lst_in)):
        if lst_in[i][j] != lst_in[j][i]:
            flag = 'NO'
            break
print(flag)
