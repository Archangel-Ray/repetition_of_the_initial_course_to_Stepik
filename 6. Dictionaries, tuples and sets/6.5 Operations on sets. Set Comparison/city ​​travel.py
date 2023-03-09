# Two lists of cities are entered each from a new line (separated by a space in the name line), which Sergey traveled
# around in the 1st and 2nd years of his trip to Russia. It is required to determine whether his route in the 2nd year
# included all the cities of the 1st year of travel? If so, print YES, otherwise NO.

a = set(input('what cities did you visit? ').split())
b = set(input('what cities are you going to visit this year? ').split())
print('YES' if a < b else 'NO')
