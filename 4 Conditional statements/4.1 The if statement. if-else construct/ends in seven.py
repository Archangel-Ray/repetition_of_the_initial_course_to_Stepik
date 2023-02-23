# Enter a four-digit number. Check that it ends with the number 7.
# Display YES if it is, and NO otherwise.

num = input('four digit number please: ')
if num[-1] == '7':
    print('YES')
else:
    print('NO')
