# Three positive integers are entered in one line separated by a space.
# Make sure that the first two numbers are the legs of a right triangle,
# and the third is its hypotenuse. (Hint: the check is done using
# the Pythagorean theorem).
# If the check passes (true), then display YES, otherwise - NO.

a, b, c = list(map(int, input('enter three positive integers: ').split()))
if a**2 == b**2+c**2 or a**2+b**2 == c**2 or a**2+c**2 == b**2:
    print('YES')
else:
    print('NO')
