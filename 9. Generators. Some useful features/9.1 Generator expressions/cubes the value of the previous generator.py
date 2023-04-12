# A positive integer a is entered. It is necessary to define a generator that would return modules of numbers
# in the range [-a; a], and then another one that would calculate the cubes of the numbers (exponentiation of 3)
# returned by the first generator.
#
# Output the first four values ​​in one line separated by a space.
# (It is assumed that the generator produces at least four values).

value = int(input("enter the number: "))
value_generator = (abs(x) for x in range(-value, value + 1))
cube_generator = (x ** 3 for x in value_generator)
counter = 0
for x in cube_generator:
    print(x, end=' ')
    counter += 1
    if counter > 3:
        break
