# Declare a function that takes one argument (a real number) and returns the square of that number.
# After the function is declared, read (using the input function) a real number and call the function with that value.
# Display the result of the function on the screen.


def get_sqrt(x):
    return x**2


n = float(input('write a number: '))
print(get_sqrt(n))
