from twython import *

from credentials import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

api_url = 'https://api.twitter.com/1.1/tweets/search/30days/ProgettoG1.json'

twitter = Twython(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)


tweets = twitter.request(api_url, method='GET', params={'q': 'from:@matteosalvinimi', 'tweet_mode': 'extended', 'count': '100'})


results = twitter.cursor(twitter.search, api_url, q='from:@matteosalvinimi', tweet_mode= 'extended', count=10000)


# for tweet in tweets:
#     print tweet['full_text']


def getTweets():
    tweets = []
    try:
        fetchedTweets = twitter.cursor(twitter.search, api_url, q='from:@matteosalvinimi', tweet_mode= 'extended', count=10000)
        for tweet in fetchedTweets:
            if tweet.full_text not in tweets:
                    tweets.append(tweet['full_text'])
        return tweets
    except Exception as e:
        print("Error : %s" % str(e))

