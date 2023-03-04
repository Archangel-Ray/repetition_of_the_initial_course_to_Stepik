# Data is entered in the key=value format in one line separated by a space. The values ​​here are integers
# (see example below). It is necessary to create a dictionary d based on them using the dict() function
# and display it on the screen with the command:
#
# print(*sorted(d.items()))

d = ['one=1', 'two=2', 'three=3']
d = [[i for i in x.split('=')] for x in d]
d = dict([[i[0], int(i[1])] for i in d])
print(*sorted(d.items()))
