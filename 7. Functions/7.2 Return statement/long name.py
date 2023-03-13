# Declare a function that takes a string (as an argument) and returns False if the string is less than 6
# characters long. Otherwise, True is returned.
#
# After the function declaration, read (using the input function) a list of city names written on a single line
# separated by a space. Then, using the list generator and the generated function, generate a list of city names
# at least six characters long from the input list. Display the result on the screen with the command:
#
# print(*lst)
#
# where lst is the resulting generated list.


def check_length(word):
    return False if len(word) < 6 else True


list_of_cities = input('write some city names: ').split()
lst = [name for name in list_of_cities if check_length(name)]
print(*lst)
