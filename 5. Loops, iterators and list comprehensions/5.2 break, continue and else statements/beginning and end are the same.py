# Enter a list of student names in one line separated by a space. Determine that at least one name in this list starts
# and ends with the same letter (case insensitive). Implement the program using a while loop and a break statement.
# Print YES if the condition is met and NO otherwise.

names = input('what names do you know? ').split()
answer = 'NO'
count = 0
while count < len(names):
    if names[count][0].lower() == names[count][-1].lower():
        answer = 'YES'
        break
    count += 1
print(answer)
