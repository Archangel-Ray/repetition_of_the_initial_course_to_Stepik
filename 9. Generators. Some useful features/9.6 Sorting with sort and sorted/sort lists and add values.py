# The input of the program receives two lists of integers (each on a separate line), written in one line separated by a
# space. List lengths can vary. The first list should be sorted in ascending order and the second in descending order.
# Add the resulting pairs from both lists to each other and get a new list of numbers. The result is displayed
# on the screen as a string of numbers separated by a space.
#
# P.S. Hint: don't forget about the zip function.

a = sorted(list(map(int, input("enter some numbers: ").split())))
b = sorted(list(map(int, input("enter some more numbers: ").split())), reverse=True)
ab = list(map(sum, zip(a, b)))
print(*ab)
