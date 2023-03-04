# A two-dimensional list is entered as a table of integers (see example below). Use list comprehension to convert
# a two-dimensional list to a one-dimensional list so that the values ​​of the elements go in reverse order.
# Display the result as a string of numbers separated by a space.

lst_in = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
print(*[lst_in[i][j] for i in range(len(lst_in)-1, -1, -1) for j in range(len(lst_in[i])-1, -1, -1)])
