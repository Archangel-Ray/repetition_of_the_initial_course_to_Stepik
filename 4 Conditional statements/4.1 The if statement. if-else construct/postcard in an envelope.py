# Four integers a, b, c, d are entered in one line separated by a space.
# Determine whether an envelope with internal dimensions a and b mm will
# fit a rectangular postcard with dimensions c and d mm. To accommodate
# a postcard in an envelope, a gap of 1 mm is required on each side.
# The card can be rotated 90 degrees.
# Output YES if included and NO if not included.

a, b, c, d = list(map(int, input('what size is your envelope and your postcard? enter four numbers: ').split()))
if (a-1 > c and b-1 > d) or (a-1 > d and b-1 > c):
    print('YES')
else:
    print('NO')
