import twitter

consumer_key = "8kpMQ4bOrZyse7UIZwWbnFnkv"
consumer_secret = "x2mUXcR3CtuYpZ62xnspwUezaqMSPGiy9GKAuSlydkv717h3kD"
access_token = "3044703939-YbNnK5McurY7Y6OLB8duKlJrVFzUlgFFieIQTc1"
access_secret = "Vikvgo4Mpn7cUUOi2Dp4yv6yqsZPCDsmVAst4plmnoxcQ"

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_secret)

results = api.GetSearch(
    raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")
print(results)