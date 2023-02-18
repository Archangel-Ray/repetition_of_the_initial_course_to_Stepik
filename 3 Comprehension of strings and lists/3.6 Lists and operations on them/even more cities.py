# The names of cities are entered in one line separated by a space.
# Based on this line, you need to create a list lst and add it to
# the end of the following list:
#
# cities = ['Moscow', 'Tver', 'Vologda']
#
# Display the result on the screen with the command:
#
# print(*lst)

cities = ["Moscow", "Tver", "Vologda"]
lst = cities + input('need city names: ').split()
print(*lst)
