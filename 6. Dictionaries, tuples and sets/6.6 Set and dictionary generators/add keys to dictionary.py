# A string with a list of grades is entered, for example:
#
# 2 unsatisfactory satisfactory good excellent
#
# The first digit is the numeric value of the first grade. The remaining estimates have numbers increasing by 1.
# Using the dictionary generator, it is necessary to form a dictionary d, where the keys will be numbers,
# and the values ​​will be words.
# For example:
#
# d = {2: 'poor', 3: 'satisfactory', 4: 'good', 5: 'excellent'}
#
# Display the value of the generated dictionary with key 4.

n, *definition = '2 unsatisfactory satisfactory good excellent'.split()
s = {i: definition[i-int(n)] for i in range(int(n), len(definition)+int(n))}

print(s[4])
