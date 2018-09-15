import indicoio
import numpy
indicoio.config.api_key = 'b3962258311d6c73574642b4877813b9'

# initialize with twitter scraper
tweets = [
    "I love writing code!",
    "Alexander and the Terrible, Horrible, No Good, Very Bad Day"
]

sentiments = indicoio.sentiment(tweets)

average_sentiment = numpy.mean(sentiments)

print("The average sentiment of tweets is: " + str(average_sentiment))
if average_sentiment > 0.5:
    print("The tweets are positive overall")
else:
    print("The tweets are negative overall")