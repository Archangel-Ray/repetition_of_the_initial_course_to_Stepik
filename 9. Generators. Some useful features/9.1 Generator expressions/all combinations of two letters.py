# Using small letters of the Latin alphabet (string ascii_lowercase):
#
# from string import ascii_lowercase
#
# write a generator that would return all combinations of two letters of the Latin alphabet.
# Print the first 50 combinations on the screen in a space-separated string.
#
# For example, the first seven initial combinations look like:
#
# aa ab ac ad ae af ag

from string import ascii_lowercase

variant_generator = (first_letter + second_letter for first_letter in ascii_lowercase
                     for second_letter in ascii_lowercase)
counter = 1
for x in variant_generator:
    print(x, end=' ')
    counter += 1
    if counter > 50:
        break
