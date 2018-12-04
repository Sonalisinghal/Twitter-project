from load_pickle import df_trump_tweets as tt, df_trump_replies as tr, df_elon_tweets as et, df_elon_replies as er
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
%matplotlib qt
  
tweetListtrump=list(tt['processed_tweet'])+list(tr['processed_tweet'])
tweetlistelon=list(et['processed_tweet'])+list(er['processed_tweet'])
stopwords = set(STOPWORDS)
stopwords.update(["REALDONALDTRUMP",'WILL','ELONMUSK'])
#removed realdonaldtrump as it occurs in every tweet and hence redundant for analysis
def make_text(l):
	text = ' '
	for val in l:
		# separate words
		tokens = val.split() 
		# Converts every word into UPPERCASE
		for i in range(len(tokens)): 
			tokens[i] = tokens[i].upper() 
		for words in tokens: 
			text = text + words + ' '
	return text

text1=make_text(tweetListtrump)
text2=make_text(tweetlistelon)

wordcloud_trump = WordCloud(background_color ='white', stopwords = stopwords, min_font_size = 1).generate(text1)
wordcloud_elon = WordCloud(background_color ='white', stopwords = stopwords, min_font_size = 1).generate(text2)  
# plot the WordCloud image                        
#plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud_trump, interpolation='bilinear') 
plt.imshow(wordcloud_elon, interpolation='bilinear') 
plt.axis("off") 
  
plt.show() 





#References
#https://www.geeksforgeeks.org/generating-word-cloud-python/