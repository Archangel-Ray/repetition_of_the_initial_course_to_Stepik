# In tasks, we several times generated a sequence of Fibonacci numbers, which is built according to the rule: each
# subsequent number is equal to the sum of the two previous ones. For a change, let's generate each subsequent number
# as the sum of the three previous numbers.
# In this case, the first three numbers are equal to 1 and we have the following sequence:
#
# 1, 1, 1, 3, 5, 9, 17, 31, 57, ...
#
# I don’t know if it has a name, therefore, within the framework of the lessons,
# I will modestly call it the Balakirev sequence.
#
# So, the input of the program is a natural number N (N 5) and it is necessary to define a generator function
# that would return the first N numbers of the Balakirev sequence (including the first three ones).
#
# Implement this feature without using collections (lists, tuples, dictionaries, etc.). Call it N times to get N
# numbers and display the resulting numbers on the screen in one line separated by a space.

n = int(input("how many numbers to print? "))


def fib_seq(what):
    sequence = []
    for _ in range(what):
        if len(sequence) < 3:
            sequence.append(1)
        else:
            sequence.append(sum(sequence[-3:]))
        yield sequence[-1]


a = fib_seq(n)
for x in a:
    print(x, end=' ')
