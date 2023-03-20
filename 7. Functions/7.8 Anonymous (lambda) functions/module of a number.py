# Declare an anonymous (lambda) function to calculate the modulus of a number (that is, negative numbers must be made
# positive). Call this function for the entered number x:
#
# x = float(input())
#
# Display the result of the function on the screen.

x = float(input("enter any number: "))
module_number = lambda number: abs(number)
print(module_number(x))
