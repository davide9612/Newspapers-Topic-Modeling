import pandas as pd
import os
from word_trends import WordTrend
from topwords import Topwords
from retweet_like_tweets import CountTweetRetweetLike

if __name__ == "__main__":

    rootdir = 'clean_scraped_tweets'

    dataframe_complete=pd.DataFrame(columns=('text', 'date', 'newspaper', 'likes', 'retweets', 'lang', 'period'))

    #iterating through all the csv files in the clean_scraped_tweets directory
    #returning a dataframe
    #dataframe is obtained by concatenating the dataframes derived from each of the csv files of the  directory

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:

            path=os.path.join(subdir, file)
            dataframe=pd.read_csv(path)
            dataframe_complete = pd.concat([dataframe,dataframe_complete])

    # calling objects of Topwords class

    # Topwords(dataframe_complete, 'it', 'precovid').show_topwords()
    Topwords(dataframe_complete,'it','precovid','corriere').show_topwords()
    # Topwords(dataframe_complete,'it','precovid','repubblica').show_topwords()
    # Topwords(dataframe_complete,'it','precovid','ilgiornale').show_topwords()
    # Topwords(dataframe_complete,'it','covid').show_topwords()
    # Topwords(dataframe_complete,'it','covid','corriere').show_topwords()
    # Topwords(dataframe_complete,'it','covid','repubblica').show_topwords()
    # Topwords(dataframe_complete,'it','covid','ilgiornale').show_topwords()
    # Topwords(dataframe_complete,'it','war').show_topwords()
    # Topwords(dataframe_complete,'it','war','corriere').show_topwords()
    # Topwords(dataframe_complete,'it','war','repubblica').show_topwords()
    # Topwords(dataframe_complete,'it','war','ilgiornale').show_topwords()
    # Topwords(dataframe_complete,'en','precovid').show_topwords()
    # Topwords(dataframe_complete,'en','precovid','wsj').show_topwords()
    # Topwords(dataframe_complete,'en','precovid','nytimes').show_topwords()
    # Topwords(dataframe_complete, 'en', 'covid').show_topwords()
    # Topwords(dataframe_complete,'en','covid','wsj').show_topwords()
    # Topwords(dataframe_complete,'en','covid','nytimes').show_topwords()
    # Topwords(dataframe_complete, 'en', 'war').show_topwords()
    # Topwords(dataframe_complete,'en','war','wsj').show_topwords()
    # Topwords(dataframe_complete,'en','war','nytimes').show_topwords()

    #calling objects of WordTrend class

    #WordTrend(dataframe_complete,'it').calculate_cfdist()
    WordTrend(dataframe_complete,'it','corriere').calculate_cfdist()
    #WordTrend(dataframe_complete,'it','repubblica').calculate_cfdist()
    #WordTrend(dataframe_complete,'it','ilgiornale').calculate_cfdist()

    #WordTrend(dataframe_complete,'en').calculate_cfdist()
    # WordTrend(dataframe_complete,'en','wsj').calculate_cfdist()
    # WordTrend(dataframe_complete,'en','nytimes').calculate_cfdist()

    #calling objects of CountTweetRetweetLike class

    #CountTweetRetweetLike(dataframe_complete,'it')
    CountTweetRetweetLike(dataframe_complete,'it','corriere')
    #CountTweetRetweetLike(dataframe_complete,'it','repubblica')
    #CountTweetRetweetLike(dataframe_complete,'it','ilgiornale')
    #CountTweetRetweetLike(dataframe_complete,'en')
    #CountTweetRetweetLike(dataframe_complete,'en','wsj')
    #CountTweetRetweetLike(dataframe_complete,'en','nytimes')