# There is a two-dimensional tuple, 5 x 5 elements in size:
#
# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
#
# A natural number N (N 5) is introduced. Based on the tuple t, it is necessary to form a new similar tuple t2
# with the size of N x N elements. The result is displayed on the screen as a table of numbers.

t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
t2 = []
n = int(input('number up to five: '))
for i in range(n):
    t_1 = ()
    for j in range(n):
        t_1 += t[i][j],
    t2.append(t_1)
for x in t2:
    print(*x)
