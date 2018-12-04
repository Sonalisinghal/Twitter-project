from pymongo import MongoClient

client = MongoClient('mongodb://localhost/twitterdb_copy')
db=client.twitterdb_copy

#list_collections = ['trump_tweets','trump_replies','elon_tweets','elon_replies']