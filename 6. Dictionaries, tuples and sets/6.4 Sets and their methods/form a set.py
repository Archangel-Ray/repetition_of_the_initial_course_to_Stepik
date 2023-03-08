# Real numbers are entered in one line separated by a space. It is necessary to form a set s on their basis.
#
# Hint: a set can be created in the same way as a list:
#
# list(map(float, list of strings of numbers ))
#
# Display the values ​​of the set s in ascending order on one line separated by a space, using the command:
#
# print(*sorted(s))

s = set(map(float, input('enter real numbers: ').split()))
print(*sorted(s))
