# Integer numbers are entered in one line separated by a space. Based on them, a tuple is formed. You need to create
# another tuple with unique (non-repeating) values ​​from the first tuple.
# Display the result as a list of numbers separated by a space.
#
# P.S. Such problems are usually solved with the help of sets, but as a practice, we will do without them for now.

numbers = tuple(map(int, input('many - many numbers: ').split()))
new_numbers = ()
for x in numbers:
    if x not in new_numbers:
        new_numbers += x,
print(*new_numbers)
