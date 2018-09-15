import indicoio
import numpy
indicoio.config.api_key = 'b3962258311d6c73574642b4877813b9'

tweets = [
    "I have a constitutional right to bear arms!",
    "I wish more candidates cared about the environment."
         ]

# initialize with twitter scraper
politics = indicoio.political(tweets)

average_politics = numpy.mean(politics)

print("The average political leaning is: " + str(average_politics))

if average_politics > 0.05:
    print("The tweets are politically leaning")

else:
    print("The tweets are not politically leaning")

    
