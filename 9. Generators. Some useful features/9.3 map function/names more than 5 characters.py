# The names of cities are entered in one line separated by a space. It is necessary to define a map function
# that would return city names only longer than 5 characters. Instead of other names - a line with a hyphen ('-').
# Form a list of the received values ​​and display it on the screen in one line separated by a space.

print(*list(map(lambda x: x if len(x)>5 else '-', input("how many city names do you know? write here: ").split())))
