#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
from credentials import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET




def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    alltweets = []
    new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode = 'extended')

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest, tweet_mode = 'extended')

        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))

        outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")] for tweet in alltweets]
        print(outtweets)

        with open('%s_tweets2.csv' % screen_name, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "created_at", "full_text"])
            writer.writerows(outtweets)

        pass

if __name__ == '__main__':
    get_all_tweets("matteosalvinimi")