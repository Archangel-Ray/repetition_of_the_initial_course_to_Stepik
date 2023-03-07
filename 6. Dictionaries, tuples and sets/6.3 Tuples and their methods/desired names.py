# The names of students are entered in one line separated by a space. Based on them, a tuple is formed.
# Display on the screen all the names in this tuple that contain 'am' (case insensitive).
# Names are displayed in one line separated by a space in lowercase (small letters).

name = tuple(input('most popular names: ').split())
print(*tuple(n.lower() for n in name if 'am' in n.lower()))
