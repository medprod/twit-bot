import tweepy
import time

consumer_key = 'qIIB1iniPVOOQeu6roC9Wi1GV'
consumer_secret = 'u37Lh4lLINOUf6GNky7oxYvtYBabNZSUfZYxCBcBLXO4KeXjti'

key = '1419951985340534792-tGu3OtqZTtkpRt9mRzvp1ENKsGTgI9'
secret = 'KFEnQyAPUmtDTpdvX7z1KpscASQN16JGZe9a1zeeROrMV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

FILE_NAME = 'last-seen.txt'

#ls = last seen

#reads file
def read_ls(FILE_NAME): 
    file_read = open(FILE_NAME, 'r')
    ls_id = int(file_read.read().strip())
    file_read.close()
    return ls_id

#write last seen id through updating it
def store_ls(FILE_NAME, ls_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(ls_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_ls(FILE_NAME), tweet_mode = 'extended')
    for tweet in reversed(tweets): #tweeting from the 1st tweet to last instead of the latest ones
        if "#botcheck" in tweet.full_text.lower():
            print("Replied To ID - " + str(tweet.id))
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Beautiful Tweet. Good Luck!", tweet.id)
            api.create_favorite(tweet.id) #likes a tweet
            api.retweet(tweet.id)
            store_ls(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15) #checks for new tweet and replies (if applicable) per given time (15 secs here)
