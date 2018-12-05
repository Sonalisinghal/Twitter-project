import plotly.plotly as py
import pandas as pd
import pycountry
from load_pickle import df_trump_tweets as tt, df_trump_replies as tr, df_elon_tweets as et, df_elon_replies as er

df = pd.read_csv('countrycodes.csv')
#print(df)
def get_country(text):
    for country in pycountry.countries:
        if country.name in text:
            return country.name
        return None

def get_all_countries(d):
    all_countries=[]
    for val in d:
        
        l=get_country(val['location'])
        if l!=None:
            all_countries.append(l)
    return all_countries

def get_occurance(d):
    all_countries=get_all_countries(d)
    frequency={}
    for l in all_countries:
        if l not in frequency:
            frequency[l]=[1]     #add country's frequency as 1
        else:
            frequency[l][0]+=1    #Increase country's frequency as 1
    return frequency


#add the code for the country
l_trump=tr['user']
l_elon=er['user']
print(get_occurance(l_elon))
print()


def plot_worldmap(l):
    
    data = [ dict(
            type = 'choropleth',
            locations = df['CODE'],  ##modify this to include list of codes of countries 
            z = [],
            text = list(country_dict.keys()),
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
    py.iplot( fig, validate=False, filename='d3-world-map' )
    return
#https://www.kaggle.com/shep312/plotlycountrycodes