# A positive integer N is entered. You need to write a recursive function called get_rec_N that displays a sequence
# of integers from 1 to N (inclusive) on the screen. Each number is displayed on a new line.
#
# The get_rec_N function must take one numeric value as a parameter. That is, to have only one parameter.
# The initial function call will look like this:
#
# get_rec_N(N)


N = int(input("enter a number: "))


def get_rec_N(n):
    if n > 0:
        get_rec_N(n-1)
        print(n)


get_rec_N(N)
