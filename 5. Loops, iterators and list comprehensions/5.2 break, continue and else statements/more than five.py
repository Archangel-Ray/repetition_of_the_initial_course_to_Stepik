# A list of city names is entered in one line separated by a space. Determine that all cities in this list are more
# than 5 characters long. Implement the program using a while loop and a break statement.
# Print YES if the condition is met and NO otherwise.

cities = input('write the names of the cities: ').split()
answer = 'YES'
count = 0
while count < len(cities):
    if len(cities[count]) < 5:
        answer = 'NO'
        break
    count += 1
print(answer)
