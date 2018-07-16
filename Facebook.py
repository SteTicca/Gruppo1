from __future__ import division

import datetime
import json

import dateutil
import facebook
import matplotlib.pyplot as plt
import numpy as np
import requests
from prettytable import PrettyTable
from textblob import TextBlob

from credentials import FACEBOOK_ACCESS_TOKEN

graph = facebook.GraphAPI(access_token=FACEBOOK_ACCESS_TOKEN, version=3.0)



def getPostsDataByDate(query, since, until, count=500):

    posts = graph.get_object(
        "%s/posts" % query,
        since=since,
        until=until,
        limit=100
    )
    postList = []
    while len(postList) < count:
        try:
            for post in posts['data']:
                if 'message' in post and len(postList) < count:
                    postList.append(post)
            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break
    return postList



if __name__ == "__main__":
    getPostsDataByDate("salviniofficial", since="1 january 2018", until="05 july 2018")