# The following menu is available:
#
# m = '''1. Introduction to Python
# 2. Lines and lists
# 3. Conditional operators
# 4. Cycles
# 5. Dictionaries, tuples and sets
# 6. Exit'''
#
# In the program, an integer from 1 to 6 is entered. It is necessary to display the menu
# item associated with this number. Implement the program using if-elif operators

m = ['',
     '1. Introduction to Python',
     '2. Lines and lists',
     '3. Conditional operators',
     '4. Cycles',
     '5. Dictionaries, tuples and sets',
     '6. Exit'
     ]
print(m[int(input('enter a number from 1 to 6: '))])
