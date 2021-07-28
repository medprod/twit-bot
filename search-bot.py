import tweepy
import time

consumer_key = 'qIIB1iniPVOOQeu6roC9Wi1GV'
consumer_secret = 'u37Lh4lLINOUf6GNky7oxYvtYBabNZSUfZYxCBcBLXO4KeXjti'

key = '1419951985340534792-tGu3OtqZTtkpRt9mRzvp1ENKsGTgI9'
secret = 'KFEnQyAPUmtDTpdvX7z1KpscASQN16JGZe9a1zeeROrMV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#searches for the last 15 tweets under this hashtag and retweets if haven't already!
hashtag = "#botcheck"
tweetNumber = 15
tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(5) #waiting 5 seconds
        except tweepy.TweepError as e:
            print(e.reason)
searchBot()