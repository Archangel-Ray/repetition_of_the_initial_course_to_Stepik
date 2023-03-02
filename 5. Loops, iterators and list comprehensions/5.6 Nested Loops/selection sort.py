# Enter a list of integers on one line separated by a space. You need to sort it by selection in ascending
# (non-decreasing) order. The idea of ​​the algorithm is very simple and is illustrated in the figure below.
#
# First, we consider the first element of the list and look for the second minimum relative to the first element
# (including it). In the figure, this is the last element with a value of -1. Then, swap the first and last elements.
# We pass to the second element of the list and repeat the same procedure, but with respect to the second element
# (that is, we do not consider the first one). In the figure, the minimum element is 2, so nothing needs to be swapped
# here. We pass to the 3rd element with a value of 6. Relative to it, we find the minimum element - this is 3.
# We swap them.
#
# Here is the idea behind the selection sort algorithm. Implement it for an input list of integers.
# Output the result as a list of numbers, one line separated by a space.

lst = list(map(int, input('multiple integers: ').split()))

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(*lst, sep=' ')
