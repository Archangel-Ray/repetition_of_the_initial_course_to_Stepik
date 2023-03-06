# Data is entered in the format:
#
# birthday 1 name_1
# birthday 2 name_2
# ...
# birthday N name_N
#
# Birthdays and names may be repeated.
# Based on them, form a dictionary and output it in the format (see the example below):
#
# birthday 1: name1, ..., nameN1
# birthday 2: name1, ..., nameN2
# ...
# birthday M: name1, ..., nameNM

lst_in = ['3 Sergey', '5 Nicholas', '4 Elena', '7 Vladimir', '5 Julia', '4 Svetlana']
d = {}
for i in lst_in:
    i = i.split()
    if i[0] not in d:
        d[i[0]] = [i[1]]
    else:
        d[i[0]].append(i[1])
for key, vol in d.items():
    print(key + ':', ', '.join(vol))
