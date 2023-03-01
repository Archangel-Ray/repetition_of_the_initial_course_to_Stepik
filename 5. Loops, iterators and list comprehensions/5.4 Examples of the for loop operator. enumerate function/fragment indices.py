# A string is entered. Need to find all indexes of fragment 'th' in the input string. Output the found indices
# into a string separated by spaces. If this fragment is never found, then print the value -1.

string = input('what do you think of our planet? ')
if 'th' not in string:
    print(-1)
else:
    for i in range(len(string)-1):
        if string[i]+string[i+1] == 'th':
            print(i, end=' ')
