'''Creates a Pandas dataframe to fetch relevant data and 
add subjectivity and polarity to each tweet'''
from pymongo import MongoClient
from textblob import TextBlob
import pandas as pd
import re, pickle

client = MongoClient('mongodb://localhost/twitterdb_copy')
db=client.twitterdb_copy
#list_collections = ['trump_tweets','trump_replies','elon_tweets','elon_replies']

#create dataframes
#for Trump and Elon Tweets
#if __name__==__main__:
cursor1 = db['trump_tweets'].find({},{'created_at':1,'id_str':1,'text':1})
df_trump_tweets =  pd.DataFrame(list(cursor1))
cursor2 = db['elon_tweets'].find({},{'created_at':1,'id_str':1,'text':1})
df_elon_tweets =  pd.DataFrame(list(cursor2))

# For replies, added 'in_reply_to_status_id_str' and 'user location'
cursor3 = db['trump_replies'].find({},{'created_at':1,'id_str':1,'text':1,'in_reply_to_status_id_str':1,'user.name':1,'user.location':1})
df_trump_replies =  pd.DataFrame(list(cursor3))
cursor4 = db['elon_replies'].find({},{'created_at':1,'id_str':1,'text':1,'in_reply_to_status_id_str':1,'user.name':1,'user.location':1})
df_elon_replies =  pd.DataFrame(list(cursor4))

#Append sentiment analysis 
#Cleans tweet text by removing links, special characters - using regex statements.
def clean_tweet(tweet):
	return ' '.join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
	#taken from https://gist.github.com/eledroos/efbe501f359d9791019b19e9ea9d60b6

def add_analysis(df):
	clean_tweets_list=[]
	subjectivity_list=[]
	polarity_list=[]
	for tweet in df['text']:
		tweetnew=clean_tweet(str(tweet))		   #clean the tweet
		clean_tweets_list.append(tweetnew)      #Append the clean tweet to a list
		analysis=TextBlob(tweetnew)       #Analyse the sentiment of the clean tweet
		subjectivity_list.append(analysis.sentiment.subjectivity)   
		polarity_list.append(analysis.sentiment.polarity)
	df_new = pd.DataFrame({'id_str': df['id_str'],'processed_tweet': clean_tweets_list,'subjectivity': subjectivity_list,'polarity': polarity_list})
	return pd.DataFrame.merge(df,df_new)

df_trump_tweets=add_analysis(df_trump_tweets)
df_elon_tweets=add_analysis(df_elon_tweets)
df_trump_replies=add_analysis(df_trump_replies)
df_elon_replies=add_analysis(df_elon_replies)

dataToStore = [df_trump_tweets, df_elon_tweets, df_trump_replies, df_elon_replies]
with open("data.pickle", "wb") as f:
	pickle.dump(dataToStore, f)
	
# for collection in list_collections:
# 	print(collection)
# 	for tweet in db[collection].find():
# 		tweetnew=clean_tweet(str(tweet['text']))
# 		analysis=TextBlob(tweetnew)
# 		subj=analysis.sentiment.subjectivity
# 		pol=analysis.sentiment.polarity
# 		#print(tweetnew,pol,subj)
# 		db[collection].updateOne(
# 			{'_id': tweet['_id']},
# 			{'$set': {'clean_tweet': tweetnew,'polarity': pol,'subjectivity': subj}})


#Word Cloud

#Spatial analysis

#Temporal analysis

#Some ideas
#sentiment analysis text blob and matplotlib
#content analysis word cloud
#Location using maps spatial analysis #no clue which library
#time analysis temporal analysis
#display using jupyter 
#might use: matplotlib, textblob, pandas, wordcloud, 

#References:
##https://www.youtube.com/watch?v=o_OZdbCzHUA  #Awesome guy Siraj Raval
#https://www.displayr.com/sentiment-analysis-simple/
#http://www.filipyoo.com/topic-and-sentiment-analysis-using-twitter-api/
#https://stackoverflow.com/questions/16249736/how-to-import-data-from-mongodb-to-pandas
