import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# To get above keys apply for twitter developer account and make an app.

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return e

auth = OAuth()
api = tweepy.API(auth)

while True:
    user = api.get_user('balveersinghyt')  # Change 'balveersinghyt' to any other twitter username
    copy = user.status.text
    try:
        api.update_status(copy)         # Post copied tweet
        print('Paste')
        time.sleep(5)

    except Exception as e:
        print(e)
        time.sleep(10)
        continue
