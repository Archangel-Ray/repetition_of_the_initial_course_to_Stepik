# The program input receives two integers a and b (a b), written in one line separated by a space.
# Define a generator that would produce modules of integers from the range [a; b].
# In a loop, output the first five values ​​of this generator. Each value on a new line.
# (It is guaranteed that there are five values).

a, b = map(int, input("enter two numbers: ").split())
module_generator = (abs(x) for x in range(a, b + 1))
counter = 0
for value in module_generator:
    print(value)
    counter += 1
    if counter > 4:
        break
