# A list of city names is entered in one line separated by a space.
# Select one city randomly from this list and display it on the screen.

import random
random.seed(1)

lst = input().split()
print(random.choice(lst))
