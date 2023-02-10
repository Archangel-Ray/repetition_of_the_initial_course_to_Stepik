# Write a program for entering two words (separated by a space in one line). Define boolean values ​​for
# the "in" operator to check if the first word occurs in the second one. And also for the operators ==, >, <.
# Combine all boolean values ​​into one line separated by a space and display on the screen.

str_1, str_2 = input('type two words: ').split()
print(str_1 in str_2, str_1 == str_2, str_1 > str_2, str_1 < str_2)
