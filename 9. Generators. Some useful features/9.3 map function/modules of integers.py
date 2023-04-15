# The input is a string of integers separated by a space. Use the map function to convert this string into a list
# of integers modulo. Form exactly the list lst from such numbers.
# Display it on the screen as a set of numbers separated by spaces.

print(*list(map(abs, map(int, input("enter multiple integers: ").split()))))
