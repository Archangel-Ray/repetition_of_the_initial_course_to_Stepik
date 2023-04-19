# It is known that the order of notes is as follows: do, re, mi, fa, sol, la, si. The input of the program receives a
# string with a set of these notes, written with a space. It is necessary to form a list from the input string with
# notes sorted in the specified way. Output the result as a string of notes separated by a space.

pattern = dict(zip(['do', 're', 'mi', 'fa', 'sol', 'la', 'si'], range(7)))
incoming = input("write notes in any order: ").split()
print(*sorted(incoming, key=lambda x: pattern[x]))
