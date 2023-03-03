# Two lists of integers of the same length are entered, each starting on a new line. Using list comprehension,
# form a third list consisting of the sum of the corresponding pairs of numbers in the lists entered.
# The result is displayed on the screen in one line separated by a space.

lst = [[int(x) for x in input('multiple numbers: ').split()],
       [int(x) for x in input('as many numbers but others: ').split()]]
print(*[lst[0][i] + lst[1][i] for i in range(len(lst[0]))])
