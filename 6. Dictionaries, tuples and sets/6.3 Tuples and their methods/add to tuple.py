# There is a tuple:
#
# t = (3.4, -56.7)
#
# Enter a sequence of integers in one line separated by a space. You need to add them to the tuple t.
# Display the result on the screen with the command:
#
# print(t)

t = (3.4, -56.7)
a = tuple(map(int, input('a few numbers: ').split()))
t += a
print(t)
