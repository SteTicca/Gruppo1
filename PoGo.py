# coding=utf-8

import re
from collections import Counter

import sys
import os
import jsonpickle
import json
import pandas as pd
import tweepy
from nltk import word_tokenize
from prettytable import PrettyTable
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from tweepy import OAuthHandler
from textblob import TextBlob

from credentials import TWITTER_ACCESS_TOKEN, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN_SECRET, TWITTER_CONSUMER_KEY

import matplotlib.pyplot as plt

auth = OAuthHandler(
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET
)

auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

if (not api):
    print("Problem connecting API")

places = api.geo_search(query = "USA", granularity = "country")

place_id = places[0].id
print('USA id is : ', place_id)

print(api.rate_limit_status()['resources']['search'])


auth = tweepy.AppAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print("Problem Connecting to API")

print(api.rate_limit_status()['resources']['search'])

searchQuery = ' #teammystic OR #teaminstinct OR #teamvalor OR' \
              '#teamblue OR #teamyellow OR #teamred OR' \
              '#mystic OR #valor OR #instinct OR' \
              '"team mystic" OR "team valor" OR "team instinct"'

maxTweets = 1000000

tweetsPerQry = 100

tweetCount = 0

with open('PoGo_USA_Tutorial.json', 'w') as f:
    for tweet in tweepy.Cursor(api.search, q=searchQuery).items(maxTweets):
        f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
        tweetCount +=1

    print("Downloaded {0} tweets".format(tweetCount))

def PrintMembers(obj):
    for attribute in dir(obj):
        if not attribute.startswith('__'):
            print(attribute)
        print

PrintMembers(tweet)


def pop_tweets(path):
    tweets = pd.DataFrame(columns=['screenName', 'userId', 'text', 'location'])
    tweets_file = open(path, 'r')
    for line in tweets_file:
        tweet = json.loads(line)
        if ('text' in tweet):
            # for i in range(0, len(tweets)):
            #     tweets.loc[i, 0] = tweet['user']['screen_name']
            #     tweets.loc[i, 1] = tweet['user']['id']
            #     tweets.loc[i, 2] = tweet['text']
            #     if ('place' is not None in tweet):
            #         tweets.loc[i, 3] = tweet['place']['full_name']
            #     else:
            #         tweets.loc[i, 3] = 'null'
            if ('place' is not None in tweet):
                tweets.loc[len(tweets)] = tweet['user']['screen_name'], tweet['user']['id'], tweet['text'], tweet['place']['full_name']
            else:
                tweets.loc[len(tweets)] = tweet['user']['screen_name'], tweet['user']['id'], tweet['text'], 'null'

    return tweets

PoGo_tweets = pop_tweets('PoGo_USA_Tutorial.json')
print('PoGo tweets dataFrame: ')
print(PoGo_tweets.head())












