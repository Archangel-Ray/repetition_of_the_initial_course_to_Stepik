# Enter a list of integers in one line separated by a space. You need to define a function that takes two arguments
# (the maximum and minimum values ​​from the list) and returns their product. Call this function and display
# the resulting numeric value on the screen.
#
# Hint: To pass arguments to a function, use the max and min functions on the input list of numbers.


def multiply(numbers):
    return min(numbers) * max(numbers)


print(multiply(list(map(int, input('write some numbers: ').split()))))
