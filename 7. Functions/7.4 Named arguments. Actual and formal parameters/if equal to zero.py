# Declare a function named get_rect_value that takes two arguments (two numbers) and another formal parameter type
# with an initial value of 0. If the type parameter is zero, then the function must return the perimeter
# of the rectangle; otherwise, its area.


def get_rect_value(a, b, type=0):
    if type == 0:
        return (a+b)*2
    else:
        return a*b


zero = int(input("zero or not zero? "))
if zero == 0:
    print(get_rect_value(int(input("enter a number: ")), int(input("enter a number: "))))
else:
    print(get_rect_value(int(input("enter a number: ")), int(input("enter a number: ")), zero))
