# Two lists of cities are entered each from a new line (in the name line separated by a space).
# It is necessary to compare them with each other for equality in unique (non-repeating) cities.
# If the lists contain the same unique cities, then display YES, otherwise - NO.

a = set(input('write some city names: ').split())
b = set(input('also write some city names: ').split())
print('YES' if a == b else 'NO')
