# A list of real numbers and a list of city names are entered, each on a separate line. It is necessary to form a
# single list lst, in which first there are numbers, and then the names of cities. Implement the program using
# the unpacking operator *. Display the resulting list on the screen with the command:
#
# print(*lst)

a = map(float, input("Enter some real numbers: ").split())
b = input("Enter multiple city names: ").split()
lst = [*a, *b]
print(*lst)
