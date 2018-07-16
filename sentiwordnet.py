from nltk.corpus import sentiwordnet as swn

# breakdown = swn.senti_synset('breakdown.n.07')
# print(breakdown)

happy = swn.senti_synsets('good', 'a')
print(happy)

