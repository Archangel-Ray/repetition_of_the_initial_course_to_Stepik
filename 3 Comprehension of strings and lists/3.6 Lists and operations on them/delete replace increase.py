# Information on the book is entered (each value on a new line):
# title, author, number of pages (integer), price (real number).
# Based on this data, a book list is formed with elements in the
# order they are entered. Then, from this list it is necessary to
# remove the 3rd element (number of pages), write 'Pushkin' as the
# author and increase the price by 2 times.
# Display the result on the screen with the command:
#
# print(book)

book = [input('enter book title: '), input('enter book author: '), int(input('how many pages are in the book? ')), float(input('how much does the book cost? '))]
del book[2]
book[1] = "Pushkin"
book[2] = book[2] * 2
print(book)
