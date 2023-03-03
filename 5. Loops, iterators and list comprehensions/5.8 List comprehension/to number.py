# Real numbers are entered into the string separated by spaces. It is necessary to form a list lst based on them using
# the list comprehension (list generator) from the modules of the entered numbers (the list should store numbers,
# not strings). Display the result as a list on the screen with the command:
#
# print(lst)

print([abs(float(x)) for x in input('multiple real numbers: ').split()])
