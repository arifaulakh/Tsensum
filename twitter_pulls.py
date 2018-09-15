import twitter
import json

class Tweet_Object:
    def __init__(self, tweetObject):
        self.tweet_object = tweetObject
        tweetDict = json.loads(json.dumps(tweetObject._json))
        self.tweet_id = tweetDict["id_str"]
        self.created_at = tweetDict["created_at"]
        self.text = tweetDict["text"]
        self.user_id = tweetDict["user"]["id_str"]
        self.user_name = tweetDict["user"]["screen_name"]
        self.user_verified = tweetDict["user"]["verified"]
        self.retweet_count = tweetDict["retweet_count"]
        self.favorite_count = tweetDict["favorite_count"]

def get_twitter_data(query):

    tweet_list = []
    id_list = []
    # twitter api setup
    consumer_key = "8kpMQ4bOrZyse7UIZwWbnFnkv"
    consumer_secret = "x2mUXcR3CtuYpZ62xnspwUezaqMSPGiy9GKAuSlydkv717h3kD"
    access_token = "3044703939-YbNnK5McurY7Y6OLB8duKlJrVFzUlgFFieIQTc1"
    access_secret = "Vikvgo4Mpn7cUUOi2Dp4yv6yqsZPCDsmVAst4plmnoxcQ"

    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)

    result_types = ["mixed", "popular", "recent"]
    for query_type in result_types:
        results = api.GetSearch(
            raw_query="q=%s&result_type=%s&count=100" % (query, query_type))

        for tweetData in results:
            tweet = Tweet_Object(tweetData)
            if tweet.user_id not in id_list:
                tweet_list.append(tweet)
                id_list.append(tweet.tweet_id)

    return tweet_list
