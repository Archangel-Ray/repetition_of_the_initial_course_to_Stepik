# Sergey's youtube account commented on another video. Some visitors left several comments. It is required to determine
# the unique number of commentators from the list of comments. Comments are received at the input of the program
# in the following format:
#
# name 1: comment 1
# name 2: comment 2
# ...
# name N: comment N
#
# It is also assumed that the names of different commentators do not match.
# Display the total number of unique commentators.

lst_in = list()
commentator = 'I'
while commentator:
    commentator = input('commentator: comment - ')
    lst_in.append(commentator)

s = set()
for w in lst_in:
    s.add(w.split(':')[0])
print(len(s))
