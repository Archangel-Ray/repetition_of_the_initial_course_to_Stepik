# Enter two natural numbers a, b (a b) in one line separated by a space. Perform the generation of an integer random
# variable in the range [a; b]. Display the result on the screen.

import random
random.seed(1)

a, b = list(map(int, input().split()))
c = random.randint(a, b)
print(c)
