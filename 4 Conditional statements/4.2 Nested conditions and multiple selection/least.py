# Enter three integers on one line separated by a space.
# It is necessary to determine the smallest among them and display it on the screen.
# Implement the program using a conditional statement without using the min function.

a, b, c = list(map(int, input('enter three digits: ').split()))
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)
