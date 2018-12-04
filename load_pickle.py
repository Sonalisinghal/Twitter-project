import pickle

with open("data.pickle", "rb") as f:
	loadedData = pickle.load(f)

df_trump_tweets = loadedData[0]
df_elon_tweets = loadedData[1]
df_trump_replies = loadedData[2]
df_elon_replies = loadedData[3]