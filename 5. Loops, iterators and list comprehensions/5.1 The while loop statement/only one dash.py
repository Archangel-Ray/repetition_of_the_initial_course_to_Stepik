# A string (slug) is entered. Replace all consecutive hyphens (--, ---, ----, etc.) on this line with single dashes (-).
# Display the result of the string conversion on the screen. Implement the program with a while loop.

new_string = ''
string = input('there are as many hyphens between words as you like: ')
index = 0
while index < len(string):
    if string[index] == '-':
        if string[index-1] == '-':
            index += 1
        else:
            new_string += string[index]
            index += 1
    else:
        new_string += string[index]
        index += 1
print(new_string)
