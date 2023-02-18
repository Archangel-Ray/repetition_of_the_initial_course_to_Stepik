# Enter: first name, last name and age (positive integer)
# each value on a new line. Using the format string method,
# it is necessary to form a string according
# to the template through the indices of variables:
#
# 'Dear <first name>, <last name>! Congratulations on your <age>th birthday!'
#
# Display the result on the screen (without quotes).

firs_name, second_name, age = input('Enter first name: '), input('Enter last name: '), input('enter age: ')
print(f'Dear {firs_name} {second_name}! Congratulations on your {age}th birthday!')
