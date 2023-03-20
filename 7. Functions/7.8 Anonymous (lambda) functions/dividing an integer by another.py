# Declare an anonymous (lambda) function with two parameters to divide one integer by another. If a division by zero
# occurs, then the function must return None, otherwise the result of the division.
#
# Assign this function to the get_div variable.

get_div = lambda a, b: a / b if b != 0 else None
print(get_div(int(input("enter a number: ")), int(input("enter a number: "))))
