# Three positive integers are entered. You can read them into variables using the command:
# It is necessary to determine whether they can be interpreted (perceived) as the lengths of the sides of the triangle. Let me remind you that the sum of the lengths of two arbitrary sides must always be greater than the third side. Display True if the triangle is formed and False otherwise. The task is done without using a conditional operator.

a, b, c = map(int, input('Enter three positive integers: ').split())
print(a+b>c and b+c>a and a+c>b)