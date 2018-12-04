import plotly.plotly as py
import plotly.graph_objs as go 
from dateutil.parser import parse
from load_pickle import df_trump_tweets as tt, df_trump_replies as tr, df_elon_tweets as et, df_elon_replies as er



# df = web.DataReader('AAPL.US', 'quandl',
#                     datetime(2007, 10, 1),
#                     datetime(2009, 4, 1))

def get_time_occurance(l):
    date_dict={}
    for d in l:
        d=parse(d)
        d=d.strftime('%b %d %Y')
        if d not in date_dict:
            date_dict[d]=1
        else:
            date_dict[d]+=1
    return date_dict
d1=get_time_occurance(tt['created_at'])
d2=get_time_occurance(tr['created_at'])
#print(d1)
name2='Trump replies'
title='Trump ANALYSER'
#print((tt['created_at']))

trace=go.Scatter(x=list(d2.keys()),y=list(d2.values()),name=name2)

data = [trace]
layout = dict(
    title=title,
   xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
       ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
   )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)




# trace = go.Scatter(x=list(df.index),
#                    y=list(df.High))

# data = [trace]
# layout = dict(
#     title='Time series with range slider and selectors',
#     xaxis=dict(
#         rangeselector=dict(
#             buttons=list([
#                 dict(count=1,
#                      label='1m',
#                      step='month',
#                      stepmode='backward'),
#                 dict(count=6,
#                      label='6m',
#                      step='month',
#                      stepmode='backward'),
#                 dict(count=1,
#                     label='YTD',
#                     step='year',
#                     stepmode='todate'),
#                 dict(count=1,
#                     label='1y',
#                     step='year',
#                     stepmode='backward'),
#                 dict(step='all')
#             ])
#         ),
#         rangeslider=dict(
#             visible = True
#         ),
#         type='date'
#     )
# )

# fig = dict(data=data, layout=layout)
# py.iplot(fig)