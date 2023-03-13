# A word is entered into the tp variable. If it is a RECT word, then declare a function named get_sq
# with two parameters that calculates the area of ​​the rectangle and returns the calculated value.
# (It should not display anything on the screen, only return a value).
#
# If the entered word is not RECT (any other), then a function with the same name get_sq is declared,
# with one parameter for calculating the square area (formula: a*a). The computed value is returned by the function.
# (It also doesn't display anything on the screen.)
#
# Note: only one function named get_sq should be defined in the program, depending on the entered word.
# You don't need to call the function, just declare it.


tp = input("write 'RECT', or don't write: ").strip()


if tp == 'RECT':
    def get_sq(a, b):
        return a * b
else:
    def get_sq(a):
        return a * a


if tp == 'RECT':
    print(get_sq(*[int(input('any number: ')) for _ in range(2)]))
else:
    print(get_sq(int(input('any number: '))))
