# Enter a list of city names in one line through a space. Iterate through all these names using a for loop and
# determine if the name of the next city begins with the last letter of the previous city in the list.
# Display YES if the sequence satisfies this rule and NO otherwise.

lst = input('do you know many cities? ').split()
answer = 'YES'
for i in range(1, len(lst)):
    if lst[i-1][-1].lower() != lst[i][0].lower():
        answer = 'NO'
        break
print(answer)
