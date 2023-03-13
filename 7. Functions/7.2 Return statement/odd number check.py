# Declare a function to check if a number is odd
# (returns True if the given number is odd and False if the number is even).
#
# After the function declaration, read (using the input function) a list of integer values ​​written on a single line,
# separated by a space. And, using the list generator and the created function, form a list of odd values ​​based
# on the input list source. Display the result on the screen with the command:
#
# print(*lst)
#
# where lst is a formed list of odd values.


def check_oddity(x):
    return True if x % 2 != 0 else False


lst = list(map(int, input('write some numbers: ').split()))
lst = [x for x in lst if check_oddity(x)]
print(*lst)
