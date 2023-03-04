# The input of the program receives data in the form of a set of strings in the format:
#
# key1=value1
# key2=value2
# ...
# keyN=valueN
#
# The keys here are integers (see the example below). It is necessary to convert them into a dictionary d
# (without using the dict() function) and display it on the screen with the command:
#
# print(*sorted(d.items()))

lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
d = {}
for x in lst_in:
    d[int(x[0])] = x[2:]
print(*sorted(d.items()))
