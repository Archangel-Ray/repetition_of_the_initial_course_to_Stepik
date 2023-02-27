# There is a one-dimensional list with a length of 10 elements, consisting of zeros:
#
# p = [0] * 10
#
# At each iteration of the loop, the user enters an integer - the index of the list element p,
# by which the value 1 is written, if it is not already there. If 1 is already set,
# then do not change the list and again ask the user for the next number.
# It is necessary to arrange five units in a list like this. (After that, the cycle is interrupted).
#
# Implement the program with a while loop and use the continue statement when 1 cannot be added to the list.
# The result is displayed on the screen as a sequence of numbers separated by a space.

p = [0] * 10
while sum(p) < 5:
    n = int(input('enter a number from 0 to 9: '))
    if p[n] == 1:
        continue
    p[n] = 1
print(*p)
