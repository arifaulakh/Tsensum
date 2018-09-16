from twitter_pulls import get_twitter_data
from collections import defaultdict
import numpy
import json
import math
import indicoio
indicoio.config.api_key = '8114b4d9ee72031b8ac0a9f7148105a6'

def get_keywords(query, level):
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
    c = 0.007 # can be changed
    minimum = c*num_tweets*math.sqrt(n)*level # can be changed
    final = {}
    for key in d2:
        if d2[key] > minimum:
            final[key.lower()] = d2[key]
    
    sentiments = indicoio.sentiment(tweet_text)
    avg_sentiment = numpy.mean(sentiments)
    return (final, avg_sentiment)

def get_graph(query):
    sentiments = {}
    query = query.lower()
    depth = 2 # can be changed
    levels = [[]]*depth
    levels[0].append(query)
    adj = defaultdict(lambda: defaultdict(lambda: {'weight': 0.0}))
    for i in range(depth):
        for j in range(len(levels[i])):
            u = levels[i][j]
            new, avg_sentiment = get_keywords(u, i + 1)
            sentiments[u] = avg_sentiment
            for v in new:
                if v == 'rt':
                    continue
                if i == depth-1 and v not in adj:
                    continue
                if v not in adj:
                    levels[i+1].append(v)
                adj[u][v]['weight'] += new[v]
                adj[v][u]['weight'] += new[v]
    adj = json.loads(json.dumps(adj)) # convert defaultdict to dict
    return (adj, sentiments)

if __name__ == "__main__":
    print(get_graph('computer science'))