from sentiment_analysis import df_trump_tweets, df_elon_tweets, df_trump_replies, df_elon_replies
import matplotlib.pyplot as plt
from matplotlib import patches
# plt.title('Sentiment analysis of Trump tweets')
# plt.subplot(1, 2, 1)
# plt.scatter(df_trump_tweets['polarity'],df_trump_tweets['subjectivity'], c=df_trump_tweets['polarity'], s=10, cmap='RdYlGn')
# plt.xlabel('Tweet polarity')
# plt.ylabel('Tweet subjectivity')
# plt.subplot(1, 2, 2)
# plt.scatter(df_trump_replies['polarity'],df_trump_replies['subjectivity'], c=df_trump_replies['polarity'], s=10, cmap='RdYlGn')
# plt.xlabel('Reply polarity')
# plt.ylabel('Reply subjectivity')
# plt.show()

plt.title('Sentiment analysis of Elon Musk tweets')
plt.subplot(2, 1, 1)
plt.scatter(df_elon_tweets['polarity'],df_elon_tweets['subjectivity'], c=df_elon_tweets['polarity'], s=10, cmap='RdYlGn')
plt.xlabel('Tweet polarity')
plt.ylabel('Tweet subjectivity')
plt.subplot(2, 1, 2)
plt.scatter(df_elon_replies['polarity'],df_elon_replies['subjectivity'], c=df_elon_replies['polarity'], s=10, cmap='RdYlGn')
plt.xlabel('Reply polarity')
plt.ylabel('Reply subjectivity')
plt.xlim(-1.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.subplots_adjust(wspace=2)
plt.show()

#donut
def plot_polarity(df_t,df_r):
	positive_polarity = [p for p in df_t if p>0]
	negative_polarity = [n for n in df_t if n<0]
	neutral_polarity = [r for r in df_t if r==0]
	total_size = len(positive_polarity) + len(negative_polarity) + len(neutral_polarity)
	n_size = len(negative_polarity)/total_size
	p_size = len(positive_polarity)/total_size
	r_size = len(neutral_polarity)/total_size
	

	labels = ['Neutral tweets', 'Positive tweets', 'Negative tweets']
	size_tweets=[20,40,40]
	size_replies=[30,60,10]
	fig, ax = plt.subplots()
	ax.axis('equal')
	#ax.legend((size_tweets[0],size_tweets[1],size_tweets[0]),('Neutral tweets', 'Positive tweets', 'Negative tweets'))
	width = 0.3
	colors=['Green','Yellow','Blue']
	pie, _ = ax.pie(size_tweets, radius=1, labels=size_tweets,colors=colors)
	plt.setp( pie, width=width, edgecolor='white')


	pie2, _ = ax.pie(size_replies, radius=1-width, labels=size_replies,labeldistance=0.7, colors=colors)
	plt.setp( pie2, width=width, edgecolor='white')
	ax.set_title("Analysis of Tweet polarity \n")
	plt.show()

tweet=[df_elon_tweets['polarity'],df_trump_tweets['polarity']]
repl=[df_elon_replies['polarity'],df_trump_replies['polarity']]
plot_polarity(tweet[0],repl[0])
plot_polarity(tweet[1],repl[1])