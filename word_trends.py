import nltk
import numpy as np


class WordTrend:
    '''
        given a specific newspaper or a group of newspapers, returns the time trend
        with which, a set of words chosen by user, occurs in newspaper's tweets
                                                                                    '''
    def __init__(self, dataframe, lang, newspaper='all newspapers'):

        self.lang = lang            #language of the newspaper (or newspapers) under analyisis
        self.newspaper = newspaper  #newspaper (or newspapers) under analysis
        self.dataframe = dataframe  #complete dataframe with all tweets of clean_scraped_tweets directory

    def calculate_cfdist(self):
        '''
            plots the time trend month by month of a specific set of words chosen by user
                                                                                        '''
        word_cfdist = nltk.ConditionalFreqDist(
            (target, tweet.date)
            for tweet in self.dataframe.itertuples()
            for w in tweet.text.split()
            for target in ['covid', 'vaccino', 'putin', 'ucraina', 'trump']
            if (w.lower() == target and (self.newspaper == tweet.newspaper or self.newspaper == 'all newspapers') and
                tweet.lang == self.lang))

        word_cfdist.plot()
        self.calculate_normalized_cfdist(word_cfdist)

    def calculate_normalized_cfdist(self, word_cfdist):
        '''
            plots the time trend month by month of a specific set of words chosen by user,
             normalized on number of tweets pubblished per month
                                                                '''
        months = sorted(list(set([tweet.date for tweet in self.dataframe.itertuples()])))
        tweets4month = [np.sum([1 for tweet in self.dataframe.itertuples()
                                if (tweet.date == month and tweet.lang == self.lang
                                and (self.newspaper == tweet.newspaper or self.newspaper == 'all newspapers'))])
                        for month in months]

        dic_tweets4month = {months[index_month]: tweets4month[index_month] for index_month in range(0, len(months))}

        for target_word in word_cfdist.values():
            for month in target_word.keys():
                target_word[month] = target_word[month]/dic_tweets4month[month]

        word_cfdist.plot()

