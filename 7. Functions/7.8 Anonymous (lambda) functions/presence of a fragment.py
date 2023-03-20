# Declare an anonymous (lambda) function to determine whether the string 'th' is present in the string passed to it.
# That is, the function must return True if such a fragment is present in the string and False otherwise.
#
# Call this function for the input string s:
#
# s = input()
#
# Display the result of the function on the screen.

s = input("what did you dream about today? ")
find_fragment = lambda text: 'th' in text
print(find_fragment(s))
