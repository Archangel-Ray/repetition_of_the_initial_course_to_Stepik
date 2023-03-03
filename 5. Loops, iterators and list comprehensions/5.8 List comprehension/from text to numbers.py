# A seven-digit positive integer is entered. Using list comprehension, form a list lst containing the digits of this
# number (numbers must be written in the list, not strings). Display the result on the screen with the command:
#
# print(lst)

print([int(x) for x in input('multi-digit number: ')])
