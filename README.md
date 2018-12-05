# Tweet Analyser

```NOTE: This is Developer Version (Please do not share with anyone without removing API Keys)```

Python Version 3.6.3
MongoDB Version v4.0.4

## Requirements
Use `pip` to install the following packages: 
* textblob
* plotly
* wordcloud
* matplotlib
* pandas
* pycountry


## Data Collection
* Import the mongoDB dump (`mongorestore`)
* The Script used for the creation of this Database can be found at `twitterdatacollect.py`

## Plots
All the plots have been added in the Jupyter Notebook. Kindly run the command `jupyter notebook` and access the file TwitterAnalysis.ipynb

## Folder Structure
* `misc` contains all the individual python scripts that were eventually combined to form the Jupyter Notebook
* `twitterdatacollect.py` was used to create the database
* `create_dataframes.py` was used to create dataframes of the relevant data collected in MongoDb
* `load_pickle.py` Use this to import the dataframes to any given file
* `TwitterAnalysis.ipynb` is the jupyter notebook used for displaying all the analysis
* `countrycodes.csv` contains countries and their codes used for plotting for spacial analysis
