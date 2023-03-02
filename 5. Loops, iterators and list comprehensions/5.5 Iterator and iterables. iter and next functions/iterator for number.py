# A four-digit positive integer is entered. Consider how you can define an iterator to iterate over its digits.
# Output the digits of this entered number (using an iterator) in one line separated by a space.

for i in iter(input('four-digit number: ')):
    print(i, end=' ')
