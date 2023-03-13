# Declare a function named is_large that takes a string (as an argument) and returns False if the string is less
# than three characters long. Otherwise, True is returned.


def is_large(line_of_text):
    return False if len(line_of_text) < 3 else True


print(is_large(input('write something: ')))
