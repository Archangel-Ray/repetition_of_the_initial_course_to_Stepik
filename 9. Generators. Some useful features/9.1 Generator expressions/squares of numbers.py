# The program input receives two integers a and b (a b), written in one line separated by a space.
# Based on them, write a generator to form squares of numbers in the range [a; b].
#
# Convert this generator to a tuple of numbers (without using loop statements)
# and assign this collection to the tp variable.
#
# P.S. You don't need to display anything on the screen, just create a tuple based on the generator.

a, b = map(int, input().split())
tp = tuple(x**2 for x in range(a, b+1))
