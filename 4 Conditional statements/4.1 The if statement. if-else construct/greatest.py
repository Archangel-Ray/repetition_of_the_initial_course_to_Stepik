# Two real numbers are entered in one line separated by a space.
# Display the largest of the numbers.
# Solve the problem using a conditional operator.

a, b = list(map(float, input('enter two real numbers: ').split()))
if a > b:
    print(a)
else:
    print(b)
