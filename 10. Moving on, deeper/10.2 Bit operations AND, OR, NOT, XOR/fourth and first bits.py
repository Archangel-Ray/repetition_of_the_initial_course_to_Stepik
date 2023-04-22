# The input to the program is a decimal integer. Using bitwise operations, turn off the 4th and 1st bits of the entered
# number. Display the resulting numeric value on the screen.

x = int(input()) & ~18
print(x)
