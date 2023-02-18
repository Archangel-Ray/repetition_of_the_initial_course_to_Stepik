# Enter: dimensions of the product (integer): width, depth,
# height - in one line separated by a space. Using the format
# method, using the keys as variable names, form the string:
# 'Dimensions: <width> x <depth> x <height>'.
# Display the result on the screen.

width, depth, height = input('enter three numbers: ').split()
print(f'Dimensions: {width} x {depth} x {height}')
