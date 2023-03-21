# Using function closures, define a nested function that increments the value of the passed parameter by 5 and returns
# the computed result. In this case, the external function must have the following signature:
#
# def counter_add(): ...
#
# Call the counter_add function and assign the result of its work to a variable named cnt. Call the internal function
# via the variable cnt with the value k entered from the keyboard:
#
# k = int(input())
#
# Display the result on the screen.

k = int(input("value: "))


def counter_add(value):
    def cnt():
        return value + 5
    return cnt


cnt = counter_add(k)
print(cnt())
