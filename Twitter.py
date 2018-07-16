# coding=utf-8

import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import re

from credentials import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

auth = OAuthHandler(
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET
)

auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitterAPI = tweepy.API(auth)

# fetchedTweets = twitterAPI.search(q="data scientist", count=1000)
# for tweet in fetchedTweets:
#     print(tweet)

def cleanTweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\ / \ / \S+)", " ", tweet).split())

def getTweetSentiment(tweet):
    analysis = TextBlob(cleanTweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def getTweetsSentiment(query, count=10):
    tweets = []
    try:
        fetchedTweets = tweepy.Cursor(twitterAPI.search, q=query).items(count)
        for tweet in fetchedTweets:
            parsed_tweet = {}
            parsed_tweet['text'] = tweet.text
            parsed_tweet['sentiment'] = getTweetSentiment(tweet.text)
            if tweet.retweet_count > 0:
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)
        return tweets
    except Exception as e:
        print("Error : %s" % str(e))

def sentimentAnalysisExample():
    tweets = getTweetsSentiment("@matteosalvinimi", count=1000)
    print len(tweets)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    print("\n\nPositive tweets:")
    for tweet in ptweets[:5]:
        print(tweet['text'])
    print("\n\nNegative tweets:")
    for tweet in ntweets[:5]:
        print(tweet['text'])

def getTweets(query, count=10):
    tweets = []
    try:
        fetchedTweets = tweepy.Cursor(twitterAPI.search, q=query, lang = "it", fromDate='2018-01-01', tweet_mode="extended").items()
        for tweet in fetchedTweets:
            if tweet.retweet_count > 0:
                if tweet.full_text not in tweets:
                    tweets.append(tweet.full_text)
            else:
                tweets.append(tweet.full_text)
        return tweets
    except Exception as e:
        print("Error : %s" % str(e))

if __name__ == '__main__':
    tweets =(getTweets("from:matteosalvinimi"))
    print(tweets)
    # file = open("190618-280618.txt", "w")
    # for i in tweets:
    #     file.write(i.encode("utf-8"))
    # file.close()