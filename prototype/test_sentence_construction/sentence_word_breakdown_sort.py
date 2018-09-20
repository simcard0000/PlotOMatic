import nltk
import numpy
import random

sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
print(tokens)
# ['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
# 'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']
tagged = nltk.pos_tag(tokens)
print(tagged)
# [('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),
# ('Thursday', 'NNP'), ('morning', 'NN')]

nouns = ['cat', 'dog', 'tree', 'river', 'sky']
sentence = []
used_indices = set()

for i in range(len(tagged)):
    print(tagged[i][1])
    if tagged[i][1] == 'NNP' or tagged[i][1] == 'NN':
        ind = random.randint(0, len(nouns)-1)
        while ind in used_indices: # prevents duplicate nouns
            ind = random.randint(0, len(nouns)-1)
        used_indices.add(ind)
        sentence.append(nouns[ind])
    # if len(used_indices) == len(nouns): # prevents all nouns being used up (should probably just reset used_indices and allow to be repeated)
        # break
    else:
        sentence.append(tagged[i][0])

print(sentence)
