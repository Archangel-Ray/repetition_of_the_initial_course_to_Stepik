# There is a dictionary with names of objects and their weight (in grams):
#
# things = { 'pencil': 20, 'mirror': 100, 'umbrella': 500, 'shirt': 300,
# 'breeches': 1000, 'paper': 200, 'hammer': 600, 'saw': 400, 'rod': 1200,
# 'comb': 40, 'pot': 820, 'tent': 5240, 'tarpaulin': 2130, 'spokes': 10}
#
# Sergey is going on a trip and is ready to put the maximum weight of N kg on his fragile shoulders
# (entered from the keyboard). He decided to put objects in the backpack in the order of their weight
# (first the heaviest, then the lightest) so that their total weight does not exceed N kg. All items are unique.
# Display a list of items (on a line separated by spaces) that Sergey will bring with him in order of decreasing weight.
#
# P. S. 1 kg = 1000 grams

things = {'pencil': 20, 'mirror': 100, 'umbrella': 500, 'shirt': 300, 'breeches': 1000, 'paper': 200, 'hammer': 600,
          'saw': 400, 'rod': 1200, 'comb': 40, 'pot': 820, 'tent': 5240, 'tarpaulin': 2130, 'spokes': 10}

n = int(input('how many kilograms can you carry? '))*1000
list_weight_things = list(things.values())
list_weight_things.sort()
take_list_weight_things = []
while n != 0:
    if list_weight_things:
        weight_thing = list_weight_things.pop()
        if weight_thing <= n:
            n -= weight_thing
            take_list_weight_things.append(weight_thing)
        else:
            continue
    else:
        break
list_things_take = []
for i in take_list_weight_things:
    for key, vol in things.items():
        if i == vol:
            list_things_take.append(key)
print(*list_things_take)
