# The names of students are entered in one line separated by a space. It is required to randomly select three students
# from this list using the sample function.
# (It is assumed that there are more than three students in the original list).
# The result is displayed on the screen in one line separated by a space.

import random
random.seed(1)

students_list = input("enter more than three names: ").split()
print(*random.sample(students_list, 3))
