# An address is entered (each meaning with a new line) in the format:
# city, street, house number (whole number), apartment number (whole number).
# Create a string according to the template:
# 'city, street, house number, apartment number', using the F-string.
# Result displayed on screen.

city, street, house, apartment = input('city: '), input('street: '), input('house: '), input('apartment: ')
print(f'c. {city}, str. {street}, h. {house}, ap. {apartment}')
