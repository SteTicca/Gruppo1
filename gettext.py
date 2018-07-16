import re

# filein = open("Salvini_Luglio.csv", "rb")
#
# fileout = open("Salvini_Luglio.txt", "w")
#
# id = re.compile("^[0-9]{19}")
#
#
# for i in filein.readlines():
#     if id.match(i.split(',')[0]) == None:
#         fileout.writelines(i.split(',')[0:])
#     else: fileout.writelines(i.split(',')[2:])
from nltk.corpus import stopwords
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

stopWords = set(stopwords.words('italian'))

# def cleanTweet():
#     tweets = []
#     file = open("Salvini_Luglio.txt", "r")
#     for i in file:
#         tweets = tweets.append(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\ / \ / \S+)", " ", i).split()))
#     return (tweets)


# def topicModeling(count=100):
#     file = cleanTweet()
#     tf_vectorizer = CountVectorizer(
#         max_df=0.95,
#         min_df=2,
#         max_features=1000,
#         stop_words=stopWords
#     )
#     tf = tf_vectorizer.fit_transform(file)
#     tf_feature_names = tf_vectorizer.get_feature_names()
#     no_topics = 10
#     lda = LatentDirichletAllocation(n_components=no_topics,
#                                     max_iter=5,
#                                     learning_method='online',
#                                     learning_offset=50.,
#                                     random_state=0).fit(tf)
#     for topic_idx, topic in enumerate(lda.components_):
#         print "Topic %d:" % (topic_idx)
#         print " ".join([tf_feature_names[i]
#                         for i in topic.argsort()[:-10 - 1:-1]])
# topicModeling()
# print(cleanTweet())

tweets = []

file = open("Salvini_Luglio.txt", "r")

tweets = file.readlines()[0].split("\r\r")
# tweets = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\ / \ / \S+)", " ", tweets).split())

lista = []
for i in tweets:
    lista.append(i)

tuobabbo = []
for w in lista:
    tuobabbo.append(' '.join(re.sub('(https://[A-Za-z0-9]*[:punct:]*)', " ", w).split()))

print(tuobabbo)