# The number of new channel subscribers by day is entered in one line
# separated by a space. Based on the entered string, it is necessary
# to form a list of integers. Then, display the maximum, minimum and
# total values ​​of this list separated by a space.

subscribers = list(map(int, input('enter some numbers: ').split()))
print(max(subscribers), min(subscribers), sum(subscribers))
