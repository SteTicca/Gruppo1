#!/usr/bin/env python
# encoding: utf-8

import tweepy
import csv
from credentials import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

endpoint = "https://api.twitter.com/1.1/tweets/search/30day/ProgettoG1.json"


def get_all_tweets(query):
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    alltweets = []

    oldest = "1017101377561120772"

    new_tweets = api.search(q = query, lang = "it", max_id = oldest, count = 200, tweet_mode = "extended")
    # new_tweets = api.search(q = query, lang = "it", count = 200, tweet_mode = "extended")

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (oldest))

        new_tweets = api.search(q = query, lang = "it", count = 200, max_id=oldest, tweet_mode = "extended")

        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1

        print ("...%s tweets downloaded so far" % (len(alltweets)))

        outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text.encode('utf-8')] for tweet in alltweets if 'retweeted_status' not in dir(tweet)]

        with open('hash8_tweets.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "created_at", "full_text"])
            writer.writerows(outtweets)

        pass

if __name__ == '__main__':
    get_all_tweets("#immigrazione OR #immigrati OR #migrazione OR #migranti")