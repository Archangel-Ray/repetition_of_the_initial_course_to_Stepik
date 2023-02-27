# (To use a while loop). Book titles are entered (each on a new line). Remove from the entered list all names
# consisting of two or more words (words in the names are separated by a space). Display the result on the screen
# as a string of the remaining names separated by a space.

lst_in = list(map(str.strip, input('What book titles do you know? (separated by commas): ').split(',')))

count = 0
while count < len(lst_in):
    if len(lst_in[count].split()) > 1:
        del lst_in[count]
        continue
    count += 1
print(*lst_in)
