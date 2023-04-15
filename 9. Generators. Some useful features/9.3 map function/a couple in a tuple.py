# The input of the program is a string in the format:
#
# key_1=value_1 key_2=value_2 ... key_N=value_N
#
# It is necessary to use the map function to convert it into a tp tuple of the form:
#
# tp = (('key_1', 'value_1'), ('key_2', 'value_2'), ..., ('key_N', 'value_N'))
#
# You don't need to display anything, just convert the string to a tuple called tp.

s = "house=дом car=машина men=человек tree=дерево"
s_lst = s.split()

tp = tuple(map(tuple, map(lambda x: x.split('='), s_lst)))
print(tp)
