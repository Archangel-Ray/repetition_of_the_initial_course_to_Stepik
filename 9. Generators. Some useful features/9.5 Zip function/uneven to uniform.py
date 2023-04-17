# A non-uniform table of integers is introduced. Using the zip function, align this table, bringing it to a rectangular
# form, discarding the outgoing elements. Display the result on the screen in the form of the same table of numbers.

lst_in = list(input("enter some numbers: ").split(' ') for _ in range(4))
aligned = zip(*list(zip(*lst_in)))
for x in aligned:
    print(' '.join(x))
