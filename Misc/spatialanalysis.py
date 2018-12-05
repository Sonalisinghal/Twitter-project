import plotly.plotly as py
import pandas as pd
import pycountry
from load_pickle import df_trump_tweets as tt, df_trump_replies as tr, df_elon_tweets as et, df_elon_replies as er

def get_country(text): #scan location text to fetch valid countries
    for country in pycountry.countries:
        if country.name in text:
            return country.name
    return None

csvFileDF = pd.read_csv('countrycodes.csv')
all_codes = {}
for index, row in csvFileDF.iterrows(): 
    c=get_country(row['COUNTRY'])
    if c!=None:
        all_codes[c]=row['CODE']

def get_all_countries(df):
    all_countries=[]    #compile all the countries in a list
    for val in df:
        l=get_country(val['location'])
        if l!=None:
            all_countries.append(l)
    return all_countries

def get_frequency(df):
    all_countries=get_all_countries(df)
    frequency={}    #Get frequency of each country
    for l in all_countries:
        if l not in frequency:
            frequency[l]=1     #add country's frequency as 1
        else:
            frequency[l]+=1    #Increase country's frequency as 1
    return frequency

def plotdata(df):
    freq=get_frequency(df)
    countries=freq.keys()
    y=[]
    z=[]
    total=0
    for country in countries:
        if country in all_codes.keys():
            y.append(all_codes[country])
            z.append(freq[country])
            c.append(country)
            total+=freq[country]
        print('Total countries that were plotted out of 10k Tweets',total)
    return y,z,c

def plot_worldmap(y,z):
    
    data = [ dict(
            type = 'choropleth',
            locations = y,  ##modify this to include list of codes of countries 
            z = z,
            text = c ,
            colorscale = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],[0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']],
            autocolorscale = False,
            reversescale = True,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
            colorbar = dict(
                autotick = False,
                tickprefix = '$',
                title = 'Spatial analysis of Replies'),
          ) ]

    layout = dict(
        title = 'Spatial analysis of Trump Tweets',
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )

    fig = dict( data=data, layout=layout )
    return fig
y,z=plotdata(tr['user'])
plot_worldmap(y,z,c)
py.iplot( fig, validate=False, filename='d3-world-map' )
#https://www.kaggle.com/shep312/plotlycountrycodes