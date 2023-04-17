# Enter a list of integers in one line separated by a space. You must leave only two-digit numbers in it.
# Implement the program using the filter function. The result is displayed on the screen as a sequence
# of the remaining numbers in one line separated by a space.

print(*list(filter(lambda x: 9 < x < 100 or -100 < x < -9, map(int, input("enter some numbers: ").split()))))
