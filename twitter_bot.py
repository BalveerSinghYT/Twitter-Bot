from os import environ
import tweepy, time

consumer_key = environ('CONSUMER_KEY')
consumer_secret = environ('CONSUMER_SECRET')
access_key = environ('ACCESS_KEY')
access_secret = environ('ACCESS_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # enter consumer_key, consumer_secret

auth.set_access_token(access_key, access_secret) # enter key, secret

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#user = api.me()

#print(user.screen_name)



"""
#This is for geting the timeline tweet from your account.
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
"""


"""
#Getting follower count and names.

name = str(input("Enter twitter @"))
user = api.get_user(name)
print("Account name:",user.screen_name)
print("Followers:", user.followers_count)
print("List:")
for friend in user.friends():
    print(friend.screen_name)
"""
user = api.me()
print(user.name)


nrTweets = 1000
count = 0
uncount = 0

deadline = 400  # No of tweets using automation
wait = 5
try:

    while count < deadline:
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
                time.sleep(2)

            except StopIteration:
                break

        #------------------------------- #Python -----------------------
        search = "#Python"
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
                time.sleep(2)

            except StopIteration:
                break

        #------------------ #coding -------------------------------
        search = "#Coding"
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
                time.sleep(3)

            except StopIteration:
                break

except tweepy.TweepError as e:
    print(e)
