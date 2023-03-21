# Using function closures, declare an inner function that increments its argument by some amount n, the parameter
# of the outer function with signature:
#
# def counter_add(n): ...
#
# Call the external function counter_add with an argument value of 2 and assign the result to the cnt variable.
# Call the internal function via the variable cnt with the value k entered from the keyboard:
#
# k = int(input())
#
# Display the result on the screen.


def counter_add(n):
    def fu(a):
        return a+n
    return fu


cnt = counter_add(2)
print(cnt(int(input("value: "))))
