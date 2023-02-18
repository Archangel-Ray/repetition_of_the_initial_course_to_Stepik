# Enter: two integers in one line separated by a space. Use the F-line
# to display them in ascending order on one line separated by a space.
# Display the result on the screen.
#
# P.S. Implement the program without using conditional statements.
# Consider how this can be done.

ab = list(map(int, input('enter two numbers: ').split()))
a = max(ab)
b = min(ab)
print(b, a)
