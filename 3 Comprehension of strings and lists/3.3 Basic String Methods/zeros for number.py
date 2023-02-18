# Enter three positive integers (maximum three-digit) separated
# by a space in one line. For two-digit and single-digit numbers,
# you need to add insignificant zeros to the left so that all numbers
# contain three digits. Display the resulting numbers in a column.

num_1, num_2, num_3 = input('enter three numbers: ').split()
print(num_1.rjust(3, '0'), num_2.rjust(3, '0'), num_3.rjust(3, '0'), sep='\n')
