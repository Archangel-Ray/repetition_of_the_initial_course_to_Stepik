# The student's grades are entered (integer numbers from 2 to 5)
# in one line separated by a space. Based on the entered string,
# a list is formed with the command:
#
# marks = list(map(int, input().split()))
#
# It is necessary to calculate the average score and display it
# on the screen with an accuracy of tenths (one decimal place).

marks = list(map(int, input('list some ratings: ').split()))
print(round(sum(marks) / len(marks), 1))
