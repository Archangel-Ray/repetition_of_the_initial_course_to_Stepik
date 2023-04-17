# A string is entered. It is required, using the entered string, to form N=10 pairs of tuples in the format:
#
# (character, ordinal index)
#
# The first index is 0. The string can be shorter than 10 characters or longer.
# That is, the number of pairs can be 10 or less. Use the zip function to form
# the specified tuples and save them to a list named lst.

s = input("write something: ")

lst = list(zip(s, range(10)))
print(lst)
