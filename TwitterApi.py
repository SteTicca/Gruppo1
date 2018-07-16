# coding=utf-8

from TwitterAPI import TwitterAPI

from credentials import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET



api = TwitterAPI(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
# r = api.request('https://api.twitter.com/1.1/tweets/search/30days/ProgettoG1.json',
#                 {'q':"from:@matteosalvinimi"}, {'since':'2018-01-01'})

r = api.request('tweets/search/30days/ProgettoG1.json', {'q':'from:matteosalvinimi', 'tweet_mode':'extended'})
for item in r.get_iterator():
    print item['full_text']
# for item in r.get_iterator():
#     print item['user']['screen_name'], item['extended_tweet']

# print(r.text)
#
# for item in r.response:
#     print(item)
#
# file = open("Salvini", "w")
# for i in r.response:
#     file.write(i.encode("utf-8"))
# file.close()