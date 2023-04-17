# Sasha and Galya collect coins. Each of them decided to write down the denominations of coins from their collection.
# There are two lists. These lists are input to the program as two strings of integers separated by a space.
# It is necessary to select the values ​​present in both lists and leave only even ones among them.
# Display the result on the screen as a string of received numbers in ascending order separated by a space.
#
# When implementing the program, use the filter function and something else (to simplify the program), think that.

sashas_collection = set(map(int, input("what coins does Sasha have? ").split()))
galyas_collection = set(map(int, input("What coins does Galya have? ").split()))
joint_collection = sashas_collection & galyas_collection
even_values = list(filter(lambda x: x % 2 == 0, joint_collection))
even_values.sort()
print(*even_values)
