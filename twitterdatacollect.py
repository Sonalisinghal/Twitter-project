import tweepy
from tweepy import AppAuthHandler
from pymongo import MongoClient

consumer_key = 'AtSpb7cH7fxCULkMZigy3w4LB'
consumer_secret = 'y7KI2sJfskZZzyQ4RhImnB3dPqaxVXp1IqNp21IxR7oATH8nVA'
#access_token = '965458435033653248-ZWv7CACfWAVQEq8bTzHlFifEijjhYmO'
#access_secret = 'L7TNG2GpyVFwlCngKTdP2RQ5cn1fmw3lfBpxg8zbJlVPA'
 
auth = AppAuthHandler(consumer_key, consumer_secret) #To increase the rate of queries
#auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if (not api): #Error handling
    print ("Problem connecting to API")

#Connect to Mongodb
client = MongoClient('mongodb://localhost/twitterdb')  #assuming there is already a database called twitterdb
db=client.twitterdb

#Gets replies to all tweets collected
def get_reply(user,list_tweet_ids):
	print("Getting Reply tweets of user "+user)
	c=0    #Counter
	for tweet in tweepy.Cursor(api.search,q='to:'+user).items():
		if 'in_reply_to_status_id_str' in tweet._json:
			if (tweet._json['in_reply_to_status_id_str'] in list_tweet_ids):
				if user=='realDonaldTrump':
					db.trump_replies.insert_one(tweet._json)
				if user=='elonmusk':
					db.elon_replies.insert_one(tweet._json)
				if(c%50==0):	
					print('Added',c)
				c+=1
				if c>=10000:
					return			
	return

#Collect posts for Trump and Elon Musk
for status in tweepy.Cursor(api.user_timeline,screen_name = 'realDonaldTrump').items():
	db.trump_tweets.insert_one(status._json)
print('Finished getting Trump tweets')


for status in tweepy.Cursor(api.user_timeline,screen_name = 'elonmusk').items():
	db.elon_tweets.insert_one(status._json)
print('Finished getting Elon tweets')

#Collecting reply to their tweets
list_trumpIDs = []
for tweet in db.trump_tweets.find():
	tweet_id=tweet['id_str']
	list_trumpIDs.append(tweet_id)
get_reply('realDonaldTrump',list_trumpIDs)
print('Finished getting Trump replies')

list_elonIDs=[]
for tweet in db.elon_tweets.find():
	tweet_id=tweet['id_str']
	list_elonIDs.append(tweet_id)
get_reply('elonmusk',list_elonIDs)
print('Finished getting Elon replies')


#References
#https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
#https://tweepy.readthedocs.io/en/v3.5.0/
#https://tweepy.readthedocs.io/en/v3.5.0/code_snippet.html#oauth
#https://stats.seandolinar.com/collecting-twitter-data-storing-tweets-in-mongodb/
#https://stackoverflow.com/questions/2693553/replies-to-a-particular-tweet-twitter-api
#https://pythondata.com/collecting-storing-tweets-with-python-and-mongodb/
#https://stellamindemography.wordpress.com/2018/05/04/mining-data-from-twitter-and-replies-to-tweets-with-tweepy/
#https://bhaskarvk.github.io/2015/01/how-to-use-twitters-search-rest-api-most-effectively./
