# A string of words separated by a space is entered. Based on them, it is necessary to compile a rectangular table of
# three columns and N rows (the number of rows is as many as possible). An extra (outgoing) word is discarded.
# Implement this program using the zip function. The result is displayed on the screen in the form of a rectangular
# table of words written with a space (in each line).

three_lists = [iter(input("write something, the more words the better: ").split())] * 3
three_columns = zip(*three_lists)
for x in three_columns:
    print(*x)
