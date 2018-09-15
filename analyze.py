from twitter_pulls import get_twitter_data
import time
import indicoio
indicoio.config.api_key = 'b3962258311d6c73574642b4877813b9'

query = 'second amendment' # replace with user input later

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

print(str(num_tweets) + ' tweets for search "' + query + '"')
print('Average sentiment: ' + str(avg_sentiment))
print('Average libertarian: ' + str(avg_libertarian))
print('Average green: ' + str(avg_green))
print('Average liberal: ' + str(avg_liberal))
print('Average conservative: ' + str(avg_conservative))