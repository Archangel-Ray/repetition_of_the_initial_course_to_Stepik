# A table of integers is entered. You must first represent this table as a two-dimensional list of numbers, and then,
# using the zip function, perform the transposition of this table (that is, replace the rows with the corresponding
# columns). Display the result on the screen as a table of numbers (the numbers in the lines follow with a space).

lst_in = list(input("enter four numbers: ") for _ in range(3))
s = list(zip(*lst_in))
for x in s:
    if x[0] == ' ':
        continue
    else:
        print(*x)
