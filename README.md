# Project- Sentiment analysis of Tweets
A sentiment analysis which uses tweets made by Donald J. trump and Elon Musk, and the replies to those. This project was done as a part of selction process for Precog- research group at IIITD.

## Data collection
twitterdatacollect.py is used for collecting the data required for sentiment analysis. 
The get_reply function collects the replies for each tweet made by the given user with specified tweet_id (is a unique integer identifying the tweet) and stores all the data in a mongodb databse, twitterdb.

## Requirements
The libraries for twitterdatacollect.py are: 
* `tweepy`
* `pymongo`


##