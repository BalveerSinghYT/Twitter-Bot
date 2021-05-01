import os
from os import environ
import tweepy, time

print("This is a Twitter Bot")
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) # enter consumer_key, consumer_secret

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET) # enter key, secret

api = tweepy.API(auth, wait_on_rate_limit=True)

#user = api.me()

#print(user.screen_name)

user = api.me()
print(user.name)


nrTweets = 1000
count = 0
uncount = 0

deadline = 700  # No of tweets using automation
wait = 20
try:
    while count < deadline:
        if count == 690:
            time.sleep(10000)
        search = "#100DaysOfCode"
        uncount = 0
        for tweet in tweepy.Cursor(api.search,search).items(nrTweets):

            if uncount == 5 or count>deadline:
                print("------------------------")
                break

            try:
                #print(status.retweeted_status.full_text)
                tweet.retweet()
                count += 1
                print("Retweet:",count, search)
                if count % 5 == 0:
                    tweet.favorite()
                    print("Favorite")
                time.sleep(wait)


            except tweepy.TweepError as e:
                #print(e.reason)
                uncount += 1
                print("Repeated:",uncount)
                time.sleep(10)

            except StopIteration:
                break

        #------------------------------- #Python -----------------------
        search = "#Coding"
        uncount = 0

        for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
            if uncount == 5 or count >deadline:
                print("------------------------")
                break
            try:
                #print(status.retweeted_status.full_text)
                tweet.retweet()
                count += 1
                print("Retweet:",count, search)
                if count % 5 == 0:
                    tweet.favorite()
                    print("Favorite")
                time.sleep(wait)


            except tweepy.TweepError as e:
                #print(e.reason)
                uncount += 1
                print("Repeated:",uncount)
                time.sleep(10)

            except StopIteration:
                break

        #------------------ #coding -------------------------------
        search = "#day code"
        uncount = 0

        for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
            if uncount == 5 or count>deadline:
                print("------------------------")
                break
            try:
                # print(status.retweeted_status.full_text)
                tweet.retweet()
                count += 1
                print("Retweet:", count, search)
                if count % 5 == 0:
                    tweet.favorite()
                    print("Favorite")
                time.sleep(wait)

            except tweepy.TweepError as e:
                # print(e.reason)
                uncount += 1
                print("Repeated:", uncount)
                time.sleep(10)

            except StopIteration:
                break

except tweepy.TweepError as e:
    print(e)
