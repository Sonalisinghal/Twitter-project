import re
from textblob import TextBlob
from load_pickle import df_trump_tweets as tt, df_trump_replies as tr
import plotly.plotly as py
import plotly.graph_objs as go

#list_collections = ['trump_tweets','trump_replies','elon_tweets','elon_replies']



trace0 = go.Scatter(
    x = tt['polarity'],
    y = tt['subjectivity'],
    name = 'Above',
    mode = 'markers',
    marker = dict(
        size = 10,
        colorscale='Viridis',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

trace1 = go.Scatter(
    x = tr['polarity'],
    y = tr['subjectivity'],
    name = 'Below',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(255, 182, 193, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = 'Sentiment analysis of Trump tweets',
              yaxis = dict(zeroline = False),
              xaxis = dict(zeroline = False)
             )

fig = dict(data=data, layout=layout)
py.iplot(data)