# A non-negative integer n is entered. It is necessary to calculate the factorial of the number n using the recursive
# function fact_rec. Let me remind you that the factorial of a number is: n! = 1 * 2 * 3 *...* n.
# The function must return a computed value.
# Declare a function with the following signature:
#
# def fact_rec(n): ...

n = int(input("enter a number: "))


def fact_rec(n):
    if n == 0:
        return 1
    return fact_rec(n-1) * n


print(fact_rec(n))
