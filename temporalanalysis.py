import plotly.plotly as py
import plotly.graph_objs as go 
from dateutil.parser import parse
from load_pickle import df_trump_tweets as tt, df_trump_replies as tr, df_elon_tweets as et, df_elon_replies as er
def get_time_occurance(l):
    date_dict={}
    for d in l:
        d=parse(d)
        d=d.strftime('%Y-%m-%d')
        if d not in date_dict:
            date_dict[d]=1
        else:
            date_dict[d]+=1
    return date_dict
d1=get_time_occurance(tt['created_at'])
d2=get_time_occurance(et['created_at'])

trace_high = go.Scatter(
    x=list(d1.keys()),
    y=list(d1.values()),
    name = "Trump tweets",
    line = dict(color = '#17BECF'),
    opacity = 0.8)

trace_low = go.Scatter(
    x=list(d2.keys()),
    y=list(d2.values()),
    name = "Elon tweets",
    line = dict(color = '#7F7F7F'),
    opacity = 0.8)

data = [trace_high,trace_low]

layout = dict(
    title='Time Series with Rangeslider',
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
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename = "Temporal Analysis of tweets")
