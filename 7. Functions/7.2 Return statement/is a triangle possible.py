# Declare a function named is_triangle that takes three sides of a triangle (integers) and checks if the given
# arguments can form a triangle. (Let me remind you that for any triangle, the length of the third side must always
# be less than the sum of the other two). If the test passes, return the Boolean value True, otherwise return False.


def is_triangle(a, b, c):
    return True if a+b > c and a+c > b and c+b > a else False


x, y, z = (int(input('write a number: ')) for _ in range(3))
print(is_triangle(x, y, z))
