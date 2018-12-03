#Sentiment analysis
from pymongo import MongoClient
from textblob import TextBlob
import pandas as pd


client = MongoClient('mongodb://localhost/twitterdb')
db=client.twitterdb

#collections=['trump_tweets','trump_replies','elon_tweets','elon_replies']
#create data
cursor = db['trump_tweets'].find({},{'created_at':1,'id_str':1,'text':1,'in_reply_to_status_id_str':1,'user.location':1})
print(list(db['trump_replies'].find({},{'user.location':1})))
df =  pd.DataFrame(list(cursor))
#print(df['entities'])

# trump_tweets=api.search('Trump')
# for t in trump_tweets:
# 	print(t.text)
# 	analysis=TextBlob(t.text)
# 	print(analysis.sentiment)












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
