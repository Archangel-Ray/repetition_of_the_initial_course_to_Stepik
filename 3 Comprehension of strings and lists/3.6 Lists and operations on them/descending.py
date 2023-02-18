# The number of new channel subscribers by day is entered in one
# line separated by a space. Based on the entered string, it is
# necessary to form a list lst of integers. It is required to sort
# the elements of this list in descending order and
# display the result on the screen with the command:
#
# print(*lst)

lst = list(map(int, input('list a few numbers: ').split()))
lst.sort(reverse=True)
print(*lst)
