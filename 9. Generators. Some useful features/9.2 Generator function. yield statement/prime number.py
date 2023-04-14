# Define a generator function that returns prime numbers.
# (A prime number is a natural number that is only divisible by itself and 1).
# Use this function to output the first 20 prime numbers (starting from 2) in one line separated by a space.


def prime_generator():
    n = 2
    while True:
        counter = 0
        for check in range(2, n):
            if n % check == 0:
                counter += 1
        if counter == 0:
            yield n
        n += 1


current_prime = prime_generator()
for _ in range(20):
    print(next(current_prime), end=' ')
