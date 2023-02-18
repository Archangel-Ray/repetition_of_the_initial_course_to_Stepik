# The names of cities are entered in one line separated by a space.
# Based on this line, you need to create a list lst and
# add it to the beginning of another list:
#
# cities = ['Moscow', 'Tver', 'Vologda']
#
# Display the result on the screen with the command:
#
# print(*lst)

lst = input('need city names: ').split()
cities = ["Moscow", "Tver", "Vologda"]
lst += cities
print(*lst)