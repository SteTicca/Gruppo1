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
    # seleziono solo i campi da visualizzare
    # richiedo l'oggetto alle API
    # Recupero i post
    posts = graph.get_object(
        "%s/posts" % query,
        since=since,
        until=until,
        limit=100
    )
    postList = []
    # Continuo ad iterare sino a quando ci sono pagine
    while len(postList) < count:
        try:
            for post in posts['data']:
                if 'message' in post and len(postList) < count:
                    postList.append(post)
            # recupero i nuovi post utilizzando i link contenuti nell'oggetto restituito
            posts = requests.get(posts['paging']['next']).json()
            # quando posts['paging'] non ha nessuna chiave 'next'
            # viene lanciata l'eccezzione KeyError e significa che non
            # ci son piu' pagine da iterare
        except KeyError:
            break
    return postList



if __name__ == "__main__":
    getPostsDataByDate("salviniofficial", since="1 january 2018", until="05 july 2018")