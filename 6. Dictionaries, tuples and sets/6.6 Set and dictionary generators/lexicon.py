# The text is entered in one line with words separated by a space. Using the set generator, generate a set of unique
# words, case-insensitive, and the length of which is at least three characters. Display the size of this set.

lexicon = {word for word in input('write an essay on the topic: my hometown - ').lower().split() if len(word) >= 3}
print(len(lexicon))
