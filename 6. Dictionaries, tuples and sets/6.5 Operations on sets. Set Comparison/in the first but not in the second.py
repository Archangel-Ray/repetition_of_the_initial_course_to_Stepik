# Two lists of integers are entered each from a new line (sets of numbers separated by a space in a line).
# It is necessary to select and display on the screen unique numbers that are present in the first list,
# but not in the second.
# Print the result on the screen as a string of numbers written in ascending order separated by a space.

a = set(map(int, input('enter some numbers: ').split()))
b = set(map(int, input('enter some more numbers: ').split()))
s = a-b
print(*sorted(s))
