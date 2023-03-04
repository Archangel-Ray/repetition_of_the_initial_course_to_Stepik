# Use the following list of strings:
#
# t = ["– Tell me, uncle, it's not for nothing",
#     "I learned Python with a channel",
#     "What did Balakirev hand out?",
#     "After all, there were combat missions,",
#     "Yes, they say, what else!",
#     "No wonder the whole of Russia remembers",
#     "How we chopped them then!"
#     ]
# You need to convert it to a two-dimensional (nested) lst list, where each line is represented by a list of words
# (words are separated by a space), but only store words longer than three characters. Solve this problem using
# list comprehension. Display the result using the command:
#
# print(lst)

t = ["– Tell me, uncle, it's not for nothing",
     "I learned Python with a channel",
     "What did Balakirev hand out?",
     "After all, there were combat missions,",
     "Yes, they say, what else!",
     "No wonder the whole of Russia remembers",
     "How we chopped them then!"
     ]
lst = [[word for word in t[i].split() if len(word) > 3] for i in range(len(t))]
print(lst)
