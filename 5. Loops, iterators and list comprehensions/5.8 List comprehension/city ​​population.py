# Enter a list in the format:
#
# <city ​​1> <population 1> <city 2> <population 2> ... <city N> <population N>
#
# It is necessary to use list comprehension to form a list lst containing nested lists of pairs:
#
# <city> <​​population>
#
# The population is an integer in thousands of people. Print the result to the screen as a list with the command:
#
# print(lst)

string = input('how many people are in the city? repeatedly: ').split()
lst = [[string[i], int(string[i+1])] for i in range(0, len(string), 2)]
print(lst)
