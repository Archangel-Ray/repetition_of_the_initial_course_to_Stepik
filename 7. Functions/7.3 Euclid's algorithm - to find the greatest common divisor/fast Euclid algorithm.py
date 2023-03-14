# The greatest common divisor (GCD) is a number that divides two numbers without remainder and divides itself without
# remainder by any other divisor of these two numbers.

import time


def get_gcd(a, b):
    """GCD is calculated for natural numbers a and b according to the fast Euclid algorithm
    :param a: first natural number
    :param b: second natural number
    :return: greatest common divisor
    """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def test_gcd(func):
    # --- test #1 -------------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    # --- test #2 -------------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    # --- test #3 -------------------
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("#test3 - ok")
    else:
        print("#test3 - fail")


test_gcd(get_gcd)
help(get_gcd)
