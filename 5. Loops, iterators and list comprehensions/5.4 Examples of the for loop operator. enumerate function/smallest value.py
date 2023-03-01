# The list is entered in the form of real numbers in one line separated by a space.
# With a for loop, you need to find the smallest value in this list.
# Display the result on the screen.
# Implement the program without using the min, max and sort functions.

string = list(map(float, input('enter some real numbers: ').split()))
m = 10**10
for i in string:
    if i < m:
        m = i
print(m)
