# A table of integers separated by a space is entered. It is necessary to shuffle the columns of this table using
# the shuffle and zip functions and display the result on the screen (also in the form of a table).

import sys
import random
random.seed(1)

lst_in = ['1 2 3 4', '5 6 7 8', '9 8 6 7']

lst_in = tuple([int(j) for j in i.split()] for i in lst_in)
lst_in = list(zip(*lst_in))
random.shuffle(lst_in)
lst_in = list(zip(*lst_in))
for arg in lst_in:
    print(*arg)
