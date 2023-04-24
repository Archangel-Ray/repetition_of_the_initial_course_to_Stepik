# There is a two-dimensional playing field of size N x N (N is a natural number, entered from the keyboard),
# presented as a nested list:
#
# P = [[0] * N for i in range(N)]
#
# It is required to randomly arrange M = 10 units (integer) in it so that they do not touch each other (that is, there
# must be zeros or a field boundary around each unit).
#
# P.S. The field does not need to be displayed on the screen (nothing needs to be displayed at all), only form.

import random

random.seed(1)
N = int(input("enter a number greater than six: "))
P = [[0] * N for i in range(N)]

for _ in range(10):
    while True:
        x = random.randrange(N)
        y = random.randrange(N)

        if P[x][y] != 1:
            if x == 0:
                if y == 0:
                    if P[x][y + 1] == 0 and P[x + 1][y] == 0 and P[x + 1][y + 1] == 0:
                        P[x][y] = 1
                        break
                if 0 < y < N - 1:
                    if P[x][y + 1] == 0 and P[x + 1][y] == 0 and P[x + 1][y + 1] == 0 and P[x][y - 1] == 0 \
                            and P[x + 1][y - 1] == 0:
                        P[x][y] = 1
                        break
                if y == N - 1:
                    if P[x][y - 1] == 0 and P[x + 1][y] == 0 and P[x + 1][y - 1] == 0:
                        P[x][y] = 1
                        break
            if 0 < x < N - 1:
                if y == 0:
                    if P[x][y + 1] == 0 and P[x + 1][y] == 0 and P[x + 1][y + 1] == 0 and P[x - 1][y + 1] == 0 \
                            and P[x - 1][y] == 0:
                        P[x][y] = 1
                        break
                if 0 < y < N - 1:
                    if P[x][y + 1] == 0 and P[x + 1][y] == 0 and P[x + 1][y + 1] == 0 and P[x][y - 1] == 0 \
                            and P[x + 1][y - 1] == 0 and P[x - 1][y] == 0 and P[x - 1][y + 1] == 0 \
                            and P[x - 1][y - 1] == 0:
                        P[x][y] = 1
                        break
                if y == N - 1:
                    if P[x][y - 1] == 0 and P[x + 1][y] == 0 and P[x + 1][y - 1] == 0 and P[x - 1][y] == 0 \
                            and P[x - 1][y - 1] == 0:
                        P[x][y] = 1
                        break
            if x == N - 1:
                if y == 0:
                    if P[x][y + 1] == 0 and P[x - 1][y + 1] == 0 and P[x - 1][y] == 0:
                        P[x][y] = 1
                        break
                if 0 < y < N - 1:
                    if P[x][y + 1] == 0 and P[x][y - 1] == 0 and P[x - 1][y] == 0 and P[x - 1][y + 1] == 0 \
                            and P[x - 1][y - 1] == 0:
                        P[x][y] = 1
                        break
                if y == N - 1:
                    if P[x][y - 1] == 0 and P[x - 1][y] == 0 and P[x - 1][y - 1] == 0:
                        P[x][y] = 1
                        break

for l in P:
    print(*l)
