from twitter_pulls import get_twitter_data
from collections import defaultdict
import json
import math
import indicoio
indicoio.config.api_key = '24a870147edb0323a7dd5bc1f2185171'

def get_keywords(query):
    tweets = get_twitter_data(query)
    tweet_text = [tweet.text for tweet in tweets]

    num_tweets = len(tweets)

    n = 5 # can be changed

    keywords = indicoio.keywords(tweet_text, version = 2, top_n = n)
    d2 = defaultdict(float)
    for d in keywords:
        for key in d:
            d2[key] += d[key] # final is sum of probabilities

    # only keep edges with high connectivity
    c = 0.01 # can be changed
    minimum = c*num_tweets*math.sqrt(n) # can be changed
    final = {}
    for key in d2:
        if d2[key] > minimum:
            final[key] = d2[key]

    return final

def get_graph(query):
    depth = 3 # can be changed
    levels = [[]]*depth
    levels[0].append(query)
    adj = defaultdict(lambda: defaultdict(lambda: {'weight': 0.0}))
    for i in range(depth-1):
        for j in range(len(levels[i])):
            u = levels[i][j]
            new = get_keywords(levels[i][j])
            for v in new:
                if v not in adj:
                    levels[i+1].append(v)
                adj[u][v]['weight'] += new[v]
                adj[v][u]['weight'] += new[v]
    return json.loads(json.dumps(adj)) # convert defaultdict to dict

