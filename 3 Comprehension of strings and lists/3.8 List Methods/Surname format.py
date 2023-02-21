# In one line, a space is entered: first name, patronymic and last name.
# It is necessary to provide this data as a new line in the format:
# Surname I.O. (For example, Sergey Mikhailovich Balakirev - Balakirev S.M.).

lst = input('enter first name, middle name and last name: ').split()
print(lst[-1], f'{lst[0][0]}.{lst[1][0]}.')
