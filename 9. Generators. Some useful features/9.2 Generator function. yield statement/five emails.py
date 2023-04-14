# A natural number N is entered. Using the strings of Latin letters ascii_lowercase and ascii_uppercase:
#
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# define a generator function that would return randomly generated email addresses with the mail.ru domain and a length
# of N characters. For example, with N=6, we get the address: SCrUZo@mail.ru
#
# To generate a random index for a chars string, use the randint function of the random module:
#
# import random
# random seed(1)
# indx = random randint(0, len(chars)-1)
#
# The generator function must return an infinite number of such addresses, that is, generate constantly.
# Print the first five generated emails and print them in a column (each on a new line).

from string import ascii_lowercase, ascii_uppercase
import random
random.seed(1)
address_length = int(input("how many characters are needed in the address? "))


def address_generator(length):
    chars = ascii_lowercase + ascii_uppercase
    mail = ''
    for _ in range(length):
        mail += random.choice(chars)
    return mail + '@mail.ru'


for _ in range(5):
    print(address_generator(address_length))
