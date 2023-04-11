# There is a program fragment (see the listing below). When executed, a FileNotFoundError is thrown.
# Write a try / except construct to display a 'File Not Found' message if the file cannot be opened.

try:
    f = open("abc.txt")
    r = f.read(1)
    f.close()
except FileNotFoundError:
    print("File Not Found")
