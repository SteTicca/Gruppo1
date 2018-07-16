# import re
#
# filein = open("hash_tweets.csv", "rb")
#
# fileout = open("hash_text.txt", "w")
#
# id = re.compile("^[0-9]{19}")
#
#
# for i in filein.readlines():
#     if id.match(i.split(',')[0]) == None:
#         fileout.writelines(i.split(',')[0:])
#     else: fileout.writelines(i.split(',')[2:])

import nltk
import string
import pattern

it_stop_words = nltk.corpus.stopwords.words('italian')
ita_stemmer = nltk.stem.snowball.ItalianStemmer()

def lemmatize_word(input_word):
    in_word = input_word
    word_it = pattern.it.parse(
        in_word,
        tokenize=False,
        tag=False,
        chunk=False,
        lemmata=True
    )
    the_lemmatized_word = word_it.split()[0][0][4]
    return the_lemmatized_word

file = open("hash_text.txt", "r")
testo = file.readlines()

word_tokenized_list = []
word_tokenized_list = word_tokenized_list.append(nltk.tokenize.word_tokenize(testo.decode("utf-8")))

print(testo[0])