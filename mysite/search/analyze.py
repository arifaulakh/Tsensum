from .twitter_pulls import get_twitter_data
import indicoio
indicoio.config.api_key = '24a870147edb0323a7dd5bc1f2185171'

def analyze(query):
    tweets = get_twitter_data(query)
    tweet_text = [tweet.text for tweet in tweets]

    num_tweets = len(tweets)

    apis = ['sentiment', 'political']
    analysis = indicoio.analyze_text(tweet_text, apis)
    # print(analysis['sentiment'])

    avg_sentiment = sum(analysis['sentiment']) / num_tweets

    avg_libertarian = sum([p['Libertarian'] for p in analysis['political']]) / num_tweets
    avg_green = sum([p['Green'] for p in analysis['political']]) / num_tweets
    avg_liberal = sum([p['Liberal'] for p in analysis['political']]) / num_tweets
    avg_conservative = sum([p['Conservative'] for p in analysis['political']]) / num_tweets

    values = (num_tweets, avg_sentiment, avg_libertarian, avg_green, avg_liberal, avg_conservative)
    return avg_sentiment
