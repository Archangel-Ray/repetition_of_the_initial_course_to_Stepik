# To the list:
#
# a = [5.4, 6.7, 10.4]
#
# add a nested list at the end with the values ​​entered into the program
# (integers are entered on the line separated by a space).
# Display the resulting list lst with the command:
#
# print(lst)

a = [5.4, 6.7, 10.4]
a.append(list(map(int, input('enter some numbers: ').split())))
print(a)
