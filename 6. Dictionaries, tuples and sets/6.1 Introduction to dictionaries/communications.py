# Phone numbers are entered in the following format:
#
# number_1 name_1
# number_2 name_2
# ...
# number_N name_N
#
# You need to create a dictionary d where the keys will be names and the values ​​will be a list of phone numbers
# for that name. Please note that the same name may belong to several different numbers.
# Output the resulting dictionary with the command:
#
# print(*sorted(d.items()))

lst_in = ['+71234567890 Sergey', '+71234567810 Sergey', '+51234567890 Mikhail', '+72134567890 Nikolay']

d = {}
for i in lst_in:
    i = i.split()
    if i[1] not in d:
        d[i[1]] = [i[0]]
    else:
        d[i[1]].append(i[0])

print(*sorted(d.items()))
