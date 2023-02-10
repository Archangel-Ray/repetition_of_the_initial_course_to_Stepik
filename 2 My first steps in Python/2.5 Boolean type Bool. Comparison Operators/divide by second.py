# Two integer values ​​are entered in one line separated by a space. Can be read with the command:
# It is necessary to determine whether the first number can be completely divided by the second. Display True if divisible and False otherwise. The task is done without using a conditional operator.

a, b = map(int, input('Two integer values ​​are entered: ').split())
print(a % b == 0)