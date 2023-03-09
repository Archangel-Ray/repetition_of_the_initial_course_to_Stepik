# Two lists of integers are entered each from a new line (sets of numbers separated by a space in a line).
# It is necessary to select and display on the screen unique numbers that are present in both the first and second
# lists at the same time. Print the result on the screen as a string of numbers written in ascending order separated
# by a space, using the command (here s is a set):
#
# print(*sorted(s))
#
# P.S. We will talk about the sorted function later, as well as the * operator. For now, just remember this ability
# to sort and display arbitrary collections on the screen.

print(*sorted(set(input('enter some numbers: ').split()) & set(input('enter some more numbers: ').split())))
