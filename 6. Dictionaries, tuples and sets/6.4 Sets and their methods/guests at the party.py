# The list of guests is fixed in the nightclub. Moreover, guests can leave the room, and then enter again.
# Then their names are fixed again. The input of the program is such a list (each name is written on a new line).
# It is required to count the total number of guests who visited the nightclub. Guests are expected to have unique
# names. Display the total number of club guests.

lst_in = list()
name = 'I'
while name:
    name = input('say the names of those you see on the carousel: ')
    lst_in.append(name)

print(len(set(lst_in)))
