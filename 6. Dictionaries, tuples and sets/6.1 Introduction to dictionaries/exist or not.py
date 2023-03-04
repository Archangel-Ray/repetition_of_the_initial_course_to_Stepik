# Data is entered in the key=value format in one line separated by a space. It is necessary to create a dictionary
# based on them, then check if there are keys with values: 'house', 'True' and '5' (all keys are strings).
# If all of them exist, then display YES, otherwise - NO.

str = 'vologda=city house=la_maison True=1 5=excellent 9=divine'
d = dict(c.split('=') for c in str.split())
lst = ['house', 'True', '5']
flag = 'YES'
for x in lst:
    if x not in d:
        flag = 'NO'
        break
print(flag)
