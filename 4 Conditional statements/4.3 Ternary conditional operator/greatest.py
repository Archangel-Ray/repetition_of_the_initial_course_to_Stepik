# Two real numbers are entered, each on a new line. It is necessary to use the ternary
# conditional operator to assign the largest value to the variable d and display it on the screen.

a, b = float(input('enter a real number: ')), float(input('enter a real number: '))
d = a if a > b else b
print(d)
