# The input of the program is a list of integers written in one line separated by a space.
# You must select the four largest unique values ​​from them. Display the result on the screen
# in descending order in one line separated by a space.

x = sorted(set(map(int, input("enter some numbers: ").split())), reverse=True)
print(*x[:4])
