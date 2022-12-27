import nltk
from prettytable import PrettyTable


class Topwords:

    """
        given: a specific newspaper or a group of newspapers; a specific period; a specific lang;
        returns: the most frequent words for that specific newspaper(s) in that specific period
                                                                                                """
    def __init__(self, dataframe, lang, period, newspaper='all newspapers'):

        self.dataframe = dataframe  #complete dataframe with all tweets of clean_scraped_tweets directory
        self.lang = lang            #language of the newspaper (or newspapers) under analyisis
        self.period = period        #historical period under analysis
        self.newspaper = newspaper  #newspaper (or newspapers) under analysis

    def show_topwords(self):
        """
            returns the most frequent words
                                            """
        fdist = nltk.FreqDist([w for tweet in self.dataframe.itertuples() for w in tweet.text.split()
                               if (tweet.lang == self.lang and tweet.period == self.period
                                   and (self.newspaper == tweet.newspaper or self.newspaper == 'all newspapers'))])

        most_common = fdist.most_common(6)
        table = PrettyTable(['Word', 'Count'])
        for t in most_common:
            table.add_row(t)

        print(table)




