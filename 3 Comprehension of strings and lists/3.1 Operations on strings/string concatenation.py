# Two integer values ​​are read into the variables a and b (entered in one line separated by a space).
# It is necessary to form a string of the form: 'Variable a = value , variable b = value ',
# using the string concatenation (connection) operator. Display the result on the screen.
# P.S. Do not use F-lines in the program.

a, b = input('enter two numbers: ').split()
print('Variable a = ' + a + ', variable b = ' + b)
