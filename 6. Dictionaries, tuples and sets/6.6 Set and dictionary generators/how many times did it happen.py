# The text is entered in one line with words separated by a space. Using set and dictionary generators,
# generate a dictionary in the following format:
#
# {word_1: number_1, word_2: number_2, ..., word_N: number_N}
#
# That is, the keys are unique words (case insensitive), and the values ​​are the number of their occurrence in the
# text. Display the dictionary value for the word (conjunction) 'and'. If there is no such key, then output 0.

essay = input('and now write an essay on the topic: how do I spend time with friends - ').lower().split()
lexicon = {word: essay.count(word) for word in essay}
print(lexicon['and'] if 'and' in lexicon else 0)
