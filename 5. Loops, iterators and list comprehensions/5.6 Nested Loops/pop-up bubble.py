# Enter a list of integers on one line separated by a space. You need to sort it in ascending (non-decreasing) using
# the pop-up bubble method. The idea of ​​the algorithm is simple and is shown in the figure below.
#
# During the first pass, we iterate over all adjacent pairs of elements, and if the value of the previous element
# (on the left) is greater than the value of the next (on the right), then they are swapped.
# (In figure 3 and 2 are reversed). The next pair is 3 and 6. They are already lined up in ascending order,
# so we do nothing and move on to the next pair of 6 and -1. We swap the values ​​and see that the last place
# is the maximum value of 6, which is what we need.
#
# On the second pass, we do the same, but we get to the penultimate element, since the last value 6 is already sorted.
# On the third pass, we exclude the last two elements, and so on. That is, in this algorithm it is enough to make N-1
# passes, where N is the length of the list.

lst = list(map(int, input('multiple integers: ').split()))

for _ in range(len(lst)-1):
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            lst[i-1], lst[i] = lst[i], lst[i-1]
print(*lst, sep=' ')
