# Phone numbers are entered in one line separated by a space with different country codes: +7, +6, +2, +4, etc.
# It is necessary to create a dictionary d, where the keys are the codes +7, +6, +2, etc., and the values ​​are a list
# of numbers (in the same order as in the input string) with the corresponding codes.
# Output the resulting dictionary with the command:
#
# print(*sorted(d.items()))

input_str = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'
phone = input_str.split()
d = {}
for i in phone:
    if i[:2] not in d:
        d[i[:2]] = [i]
    else:
        d[i[:2]].append(i)

print(*sorted(d.items()))
