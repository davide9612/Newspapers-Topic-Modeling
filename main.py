from italian_cleaning import ItalianCleaner
from english_cleaning import EnglishCleaner

import pandas as pd
import os



if __name__ == "__main__":

    dataframes = {}
    rootdir = 'scraped_tweets'

    # iterating all csv files in scraped_tweets directory
    # creating a dictionary in which for each csv file are saved: dataframe from csv; file path; file name

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            path=os.path.join(subdir, file)
            dataframes[file]={'dataframe':pd.read_csv(path),'path': subdir,'file_name':file}

    #calling Italian_Cleaner class for each csv file that contains italian tweets
    #calling English_Cleaner class for each csv file that contains english tweets

    for dframe in dataframes.values():
        df = dframe['dataframe']
        path = dframe['path']
        file_name = dframe['file_name']

        if file_name.endswith('it.csv'):
            ItalianCleaner(df, path, file_name).pipeline()

        if file_name.endswith('en.csv'):
            EnglishCleaner(df, path, file_name).pipeline()