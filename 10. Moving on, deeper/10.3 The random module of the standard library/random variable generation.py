# Enter two natural numbers a, b (a b) in one line separated by a space. Perform the generation of a real random
# variable in the range [a; b). Round the result to hundredths and display it on the screen.

import random
random.seed(1)

a, b = list(map(int, input().split()))
c = random.uniform(a, b)
print(round(c, 2))
