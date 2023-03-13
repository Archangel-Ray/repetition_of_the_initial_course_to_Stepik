# Declare a function to check if a number is even
# (returns True if the given number is even and False if the number is odd).
#
# After declaring the function in the loop, it is necessary to read an integer numeric value (using the input function)
# until the number 1 arrives. If the read value is even (checked using the given function), then it is displayed
# on the screen (in a column, that is, each value from a new line ).


def parity_checks(number):
    return True if number % 2 == 0 else False


received_number = int(input('what number do you know? '))
while received_number != 1:
    if parity_checks(received_number):
        print(received_number)
    received_number = int(input('what other number do you know? '))
