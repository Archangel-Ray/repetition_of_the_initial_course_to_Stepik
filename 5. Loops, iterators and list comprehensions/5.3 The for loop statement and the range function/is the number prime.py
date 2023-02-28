# A natural number n is entered. Use a for loop to determine if it is prime (that is, only divisible by itself and 1).
# Display YES if n is prime and NO otherwise.

n = int(input('enter a number: '))
answer = 'YES'
for i in range(2, n):
    if n % i == 0:
        answer = 'NO'
        break
print(answer)
