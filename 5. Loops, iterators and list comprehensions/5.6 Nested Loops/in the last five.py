# A natural number N is entered (that is, a positive integer).
# It is required to create a two-dimensional (nested) list of N x N elements, consisting of all ones,
# and then write fives in the last column. Display this list on the screen as a table of numbers,
# as shown in the example below.
#
# P.S. Be careful at the end of the lines of spaces should not be!

n = int(input('digit: '))
main_list = [[1 for _ in range(n)] for i in range(n)]
for i in range(len(main_list)):
    main_list[i][-1] = 5
for i in main_list:
    print(*i)
