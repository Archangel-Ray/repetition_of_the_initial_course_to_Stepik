# The names of cities are entered in one line separated by a space. Based on them, a tuple is formed.
# If this tuple contains the city 'Chicago', then this element should be deleted (creating a new tuple).
# Output the result to the screen as a string with city names separated by a space.

cities = tuple(input('what cities do you know? ').split())
u = "Chicago"
if u in cities:
    cities = tuple(i for i in cities if i != u)
print(*cities)
