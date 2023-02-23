# Enter a six-digit number. Determine if it is happy.
# (A lucky number is a six-digit number in which the sum of its
# first three digits is equal to the sum of its last three digits.).
# Output YES if happy and NO otherwise.

numbers = list(map(int, list(input('enter a six-digit number: '))))
if sum(numbers[:3]) == sum(numbers[3:]):
    print('YES')
else:
    print('NO')
