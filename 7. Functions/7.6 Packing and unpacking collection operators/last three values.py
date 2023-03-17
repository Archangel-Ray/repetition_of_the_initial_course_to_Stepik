# A list of seven integers is entered in one line separated by a space. It is necessary to enter the first four
# numbers into the variable lst, and the remaining three into separate variables x, y, z. Make using the packing
# operator. Print the lst list to the screen with the command:
#
# print(*lst)

*lst, x, y, z = map(int, input("write seven numbers: ").split())
print(*lst)
