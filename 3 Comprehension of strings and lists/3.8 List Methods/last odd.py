# Integer numbers are entered in one line separated by a space.
# It is necessary to convert them to the list lst , then remove
# the last value and if it is odd, then add True to the list (at the end),
# otherwise - False. Display the resulting list on the screen with the command:
#
# print(*lst)
#
# Execute the program without using a conditional statement.

lst = list(map(int, input('Enter whole numbers: ').split()))
end = lst.pop()
end = end%2!=0
lst.append(end)
print(*lst)
