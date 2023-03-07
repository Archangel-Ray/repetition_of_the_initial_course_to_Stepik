# Integer numbers are entered in one line separated by a space. Based on them, a tuple is formed. You need to find and
# display all indices of non-unique (duplicate) values ​​in this tuple.
# Display the result as a string of numbers separated by spaces.

numbers = tuple(map(int, input('write some numbers: ').split()))
tuple_indexes = ()
for i in range(len(numbers)):
    if numbers.count(numbers[i]) > 1:
        tuple_indexes += i,

print(*tuple_indexes)
