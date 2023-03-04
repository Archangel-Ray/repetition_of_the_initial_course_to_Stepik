# Data is entered in the key=value format in one line separated by a space. It is necessary to create a dictionary d
# based on them, then remove the keys 'False' and '3' from this dictionary, if they exist.
# The keys and values ​​of a dictionary are strings. Display the resulting dictionary on the screen with the command:
#
# print(*sorted(d.items()))

str = 'Elena=name don=river moscow=city False=false 3=satisfactory True=true'
d = dict(c.split('=') for c in str.split())
lst = ['False', '3']
for x in lst:
    if x in d:
        del d[x]
print(*sorted(d.items()))
