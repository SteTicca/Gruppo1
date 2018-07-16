from TwitterAPI import TwitterAPI
import csv
import json
from credentials import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET


twitter = TwitterAPI(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)



def get_all_tweets(query):
    alltweets = []
    new_tweets = twitter.request('tweets/search/30day/:ProgettoG1', {'query': query, 'maxResults': 100,'fromDate':201806100000, "toDate":201806300000, "is:retweet":False})
    # if json.loads(new_tweets.text)["next"]:
    #     next = json.loads(new_tweets.text)["next"]
    #     while (tweet["created_at"] != "Sun Jun 11 00:00:00 +0000 2018" for tweet in new_tweets):
    #         new_tweets = twitter.request('tweets/search/30day/:ProgettoG1', {'query': query, 'maxResults':100, 'fromDate':201806100000, "toDate":201806300000, "is:retweet":False, "next":next})
    #         alltweets.extend(tweet for tweet in new_tweets)
    #         next = json.loads(new_tweets.text)["next"]
    # else:
    #     pass
    alltweets.extend(tweet for tweet in new_tweets)
    outtweets = [[tweet["id_str"], tweet["created_at"],tweet["text"].encode('utf-8')] for tweet in alltweets if'RT' not in tweet["text"]]

    with open('prova.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "full_text"])
        writer.writerows(outtweets)
    # print(json.loads(new_tweets.text)["next"])
    # alltweets.append(new_tweets)
    # print(alltweets)
    # # print(new_tweets)
    # print(alltweets)

    # oldest = alltweets[-1]["statuses"][0]["id"] -1


    # while len(new_tweets) > 0:
    #     print "getting tweets before %s" % (oldest)
    #
    #     #all subsiquent requests use the max_id param to prevent duplicates
    #     new_tweets = twitter.search(q = query, lang = "it", count = 200, max_id=oldest, tweet_mode = "extended")
    #
    #     #save most recent tweets
    #     alltweets.append(new_tweets)
    #
    #     #update the id of the oldest tweet less one
    #     oldest = alltweets[-1]["statuses"][0]["id"] - 1
    #
    #     print "...%s tweets downloaded so far" % (len(alltweets))
    #
    #     outtweets = [[tweet["statuses"][0]["id_str"], tweet["statuses"][0]["created_at"], tweet["statuses"][0]["full_text"].encode('utf-8')] for tweet in alltweets if 'retweeted_status' not in tweet["statuses"][0]]
    #
    #     with open('prova.csv', 'wb') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(["id", "created_at", "full_text"])
    #         writer.writerows(outtweets)
    #
    #     pass

if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("#immigrazione OR #immigrati OR #migrazione OR #migranti")