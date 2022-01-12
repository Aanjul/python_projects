# For refrence https://github.com/Logan1x/Python-Scripts/blob/master/bin/twitter_retweet_bot.py

# For refrence https://github.com/Logan1x/Python-Scripts

import tweepy # This is a Twitter API helper
import time


# You should get the following keys and authentication codes for your Twitter account
# Visit apps.twitter.com
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

# Twitter requires 0Auth2 authentication. You can readup about this.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def retweet_bot():
	for tweet in tweepy.Cursor(api.search, q='Hashtag to listen for').item(10):
		try:
			print('Twitter user: ' + '@' + tweet.user.screen_name)
			tweet.retweet()
			print('\nDone')
			# You can remove the time module, if you want the program to continously retweet
			time.sleep(5)
		except tweepy.error.TweepError:
			pass
			
if __name__ == '__main__':
	retweet_bot()