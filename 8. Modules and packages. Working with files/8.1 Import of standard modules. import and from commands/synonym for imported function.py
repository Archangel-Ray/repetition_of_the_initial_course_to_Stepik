# From the random module, import only two functions: seed and random, but the latter must have a synonym for rnd
# (the name through which it will be called in the program). Execute these functions in the program as follows:
#
# seed(10)
# print(round(rnd(), 2))

from random import seed, random as rnd

seed(10)
print(round(rnd(), 2))
