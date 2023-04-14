# A natural number N (N 8) is introduced. It is necessary to define a generator function that would produce a password
# of length N characters from random letters, numbers, and some other characters. To obtain a sequence of valid
# characters for generating passwords, the program imported two strings: ascii_lowercase, ascii_uppercase
# (see the listing below), on the basis of which the general list is formed:
#
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + '0123456789!?@#$*'
#
# The generator function must, on each call, return a new password from randomly selected chars of length N and do
# this indefinitely, that is, it can be called an infinite number of times. Generate random index indx in
# range [a; b] for a character using the randint function of the random module:
#
# import random
# random seed(1)
# indx = random randint(a, b)
#
# Use this function to generate the first five passwords and print them in a column (each on a new line).

import random
from string import ascii_lowercase, ascii_uppercase

random.seed(1)
password_length = int(input("how many characters are in the password? "))


def password_generator(length):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password


for _ in range(5):
    print(password_generator(password_length))
