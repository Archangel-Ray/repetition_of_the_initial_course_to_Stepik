# A two-dimensional list of 5 x 5 elements is entered, consisting of zeros and, in some positions,
# ones (see the input example below). It is required to check whether the units touch each other horizontally,
# vertically and diagonally. That is, there must be zeros around each one.
# If the test passes, output YES, otherwise NO.
#
# P.S. To read the entire list, the program has already written the initial lines.

lst_in = [[1, 0, 0, 0, 0],
          [0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 1, 0, 1, 0],
          [0, 0, 0, 0, 0]
          ]

flag = 'YES'
for i in range(len(lst_in)-1):
    if flag == 'NO':
        break
    for j in range(len(lst_in)-1):
        if lst_in[i][j] + lst_in[i][j+1] + lst_in[i+1][j] + lst_in[i+1][j+1] > 1:
            flag = 'NO'
            break
print(flag)
