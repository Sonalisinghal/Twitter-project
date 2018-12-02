import tweepy
from tweepy import OAuthHandler
from pymongo import MongoClient
import json

 
consumer_key = 'AtSpb7cH7fxCULkMZigy3w4LB'
consumer_secret = 'y7KI2sJfskZZzyQ4RhImnB3dPqaxVXp1IqNp21IxR7oATH8nVA'
access_token = '965458435033653248-ZWv7CACfWAVQEq8bTzHlFifEijjhYmO'
access_secret = 'L7TNG2GpyVFwlCngKTdP2RQ5cn1fmw3lfBpxg8zbJlVPA'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_reply(user,tweet_id):
	replies=[]
	# for full_tweets in tweepy.Cursor(api.user_timeline,screen_name=user).items():
	for tweet in tweepy.Cursor(api.search,q='to:'+user,since_id=tweet_id).items():
		if 'in_reply_to_status_id_str' in tweet._json:
			if (tweet._json['in_reply_to_status_id_str']==tweet_id):
				print(tweet._json['text'])
				replies.append(tweet._json)	
				print(len(replies))
				if len(replies)>100:
					return replies			
	return replies

#Posts for Trump and Elon Musk
user_trump=[]
user_elon=[]
for status in tweepy.Cursor(api.user_timeline,screen_name = 'realDonaldTrump').items(10):
	user_trump.append(status._json)
for status in tweepy.Cursor(api.user_timeline,screen_name = 'elonmusk').items(10):
	user_elon.append(status._json)

#Collecting reply to their tweets
reply_trump=[]
reply_elon=[]
c=0
for tweet in user_trump:
	tweet_id=tweet['id_str']
	print(tweet_id)
	print('\n',tweet['text'])
	reply_trump.append(get_reply('realDonaldTrump',tweet_id))
	print('reply trump',len(reply_trump[c]))
	c+=1

for tweet in user_elon:
	tweet_id=tweet['id_str']
	reply_elon.append(get_reply('elonmusk',tweet_id))

#References
#https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
#https://tweepy.readthedocs.io/en/v3.5.0/
#https://tweepy.readthedocs.io/en/v3.5.0/code_snippet.html#oauth
#https://stats.seandolinar.com/collecting-twitter-data-storing-tweets-in-mongodb/
#https://stackoverflow.com/questions/2693553/replies-to-a-particular-tweet-twitter-api
#https://pythondata.com/collecting-storing-tweets-with-python-and-mongodb/
#https://stellamindemography.wordpress.com/2018/05/04/mining-data-from-twitter-and-replies-to-tweets-with-tweepy/
