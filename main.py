import os
import pandas as pd

from topic_skl import TopicScikit
from topic_gsm import TopicGensim

if __name__ == "__main__":

    rootdir = 'clean_scraped_tweets'

    dataframe_complete = pd.DataFrame(columns=('text', 'date', 'newspaper', 'likes', 'retweets', 'lang', 'period'))

    # iterating through all the csv files in the clean_scraped_tweets directory
    # returning a dataframe
    # dataframe is obtained by concatenating the dataframes derived from each of the csv files of the  directory

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            path = os.path.join(subdir, file)
            dataframe = pd.read_csv(path)
            dataframe_complete = pd.concat([dataframe, dataframe_complete])

    #before call objects, from terminal enter the command: mkdir topic_parameters

    #calling objects of class TopicScikit

    TopicScikit(dataframe_complete, 'precovid', 'it', "repubblica").topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'precovid', 'it', "corriere").topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'precovid', 'it', "ilgiornale").topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'precovid', 'it').topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'covid', 'it', "repubblica").topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'covid', 'it', "corriere").topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'covid', 'it', "ilgiornale").topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'covid', 'it').topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'war', 'it', "repubblica").topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'war', 'it', "corriere").topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'war', 'it', "ilgiornale").topic_modeling_starter()
    # TopicScikit(dataframe_complete, 'war', 'it').topic_modeling_starter()
    # TopicScikit(dataframe_complete,'precovid','en','wsj').topic_modeling_starter()
    # TopicScikit(dataframe_complete,'precovid','en','nytimes').topic_modeling_starter()
    # TopicScikit(dataframe_complete,'precovid','en').topic_modeling_starter()
    # TopicScikit(dataframe_complete,'covid','en','wsj').topic_modeling_starter()
    # TopicScikit(dataframe_complete,'covid','en','nytimes').topic_modeling_starter()
    # TopicScikit(dataframe_complete,'covid','en').topic_modeling_starter()
    # TopicScikit(dataframe_complete,'war','en','wsj').topic_modeling_starter()
    # TopicScikit(dataframe_complete,'war','en','nytimes').topic_modeling_starter()
    # TopicScikit(dataframe_complete,'war','en').topic_modeling_starter()

    #Calling objects of class TopicGensim

    TopicGensim(dataframe_complete, 'precovid', 'it', "repubblica").topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'precovid', 'it', "corriere").topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'precovid', 'it', "ilgiornale").topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'precovid', 'it').topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'covid', 'it', "repubblica").topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'covid', 'it', "corriere").topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'covid', 'it', "ilgiornale").topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'covid', 'it').topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'war', 'it', "repubblica").topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'war', 'it', "corriere").topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'war', 'it', "ilgiornale").topic_modeling_starter()
    # TopicGensim(dataframe_complete, 'war', 'it').topic_modeling_starter()
    # TopicGensim(dataframe_complete,'precovid','en','wsj').topic_modeling_starter()
    # TopicGensim(dataframe_complete,'precovid','en','nytimes').topic_modeling_starter()
    # TopicGensim(dataframe_complete,'precovid','en').topic_modeling_starter()
    # TopicGensim(dataframe_complete,'covid','en','wsj').topic_modeling_starter()
    # TopicGensim(dataframe_complete,'covid','en','nytimes').topic_modeling_starter()
    # TopicGensim(dataframe_complete,'covid','en').topic_modeling_starter()
    # TopicGensim(dataframe_complete,'war','en','wsj').topic_modeling_starter()
    # TopicGensim(dataframe_complete,'war','en','nytimes').topic_modeling_starter()
    # TopicGensim(dataframe_complete,'war','en').topic_modeling_starter()