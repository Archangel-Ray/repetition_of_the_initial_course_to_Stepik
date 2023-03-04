# Repeat the task of transposing a rectangular matrix using the list comprehension set out in the video tutorial
# for this practice. The input is a table of integers, at the output you need to display the same table in transposed
# form (rows are replaced by columns), using the command:
#
# for row in A:
#     print(*row)
#
# where A is the transposed 2D list. It is advisable to do this task without reviewing the video.

lst_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]]

A = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]
for row in A:
    print(*row)
