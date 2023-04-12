# There is a graph of the function f(x) = 0.5x^2 - 2. It is necessary to write a generator that would produce
# the values ​​of this function for the argument x in the range [a; b] with a step of 0.01.
# The values ​​a, b are entered from the keyboard in one line separated by a space as integers (a b).
# Display the first 20 values ​​of the function, accurate to hundredths, taken from the generator.
#
# P.S. Function values ​​are calculated by the command:
#
# f(x) = 0.5 * pow(x, 2) - 2.0

a, b = map(int, input("enter two numbers: ").split())
function_values = (0.5 * pow(x / 100, 2) - 2.0 for x in range(100 * a, 100 * b + 1))
for _ in range(20):
    print(round(next(function_values), 2), end=' ')
