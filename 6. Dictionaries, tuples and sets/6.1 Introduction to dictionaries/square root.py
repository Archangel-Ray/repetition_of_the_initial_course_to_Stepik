# The user enters positive integer numbers in a loop until he enters the number 0. For each number, the square root
# is calculated (accurate to hundredths) and the value is displayed on the screen (in a column). Using a dictionary,
# cache the data so that when you enter the same number again, the result is not calculated, but the previously
# calculated value from the dictionary is taken. In this case, the screen should display:
#
# value from cache: <number>

d = {}
n = int(input('number: '))
while n != 0:
    if n not in d:
        x = round(n**0.5, 2)
        d[n] = x
        print(x)
    else:
        print('value from cache:', d[n])
    n = int(input('number: '))
