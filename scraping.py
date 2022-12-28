import os
import sys
import pandas as pd
import snscrape.modules.twitter as sntwitter
import time


class Tweetscraper:

    '''
        Class Tweetscraper allows, in the specified time interval, to scrape tweets from a specific official
        account of a newspaper.

        Courtesy notice: this code allows, in case of need, to stop manually scraping and obtain the date
        of last extracted tweet. If you want to exploit this opportunity:
        If your operating system is Linux:
            the date is returned automatically when you stop the code
        If your operating system is Windows:
            please go to Run-->edit configuration -->emulate terminal in output console
            to stop the code press CTRL+c
                                        '''


    def __init__(self, newspaper, start, end, period, tweets2sleep, sleeping_time, lang, path, n_tweets=float('inf')):

        self.newspaper = newspaper          # the official newspaper account from which you want to scrape tweets;
        self.start = start                  # date since you want to scrape tweets
        self.end = end                      # date until you want to scrape tweets
        self.period = period                # historical period of the chosen dates;
        self.tweets2sleep = tweets2sleep    # limit of tweets to be scraped before suspending scraping;
        self.sleeping_time = sleeping_time  # suspension time when the specified tweets2sleep limit is reached;
        self.lang = lang                    # language of tweets you want to scrape;
        self.path = path                    # path of csv file where you want to save scraped tweets;
        self.n_tweets = n_tweets            #limit of tweets you want to scrape calling the object. By default is inf;

    def create_csv(self, df):
        '''
            creates csv file to save scraped tweets
            '''
        path = self.path
        if not os.path.exists(path): os.makedirs(path)
        df.to_csv(f'{path}/{self.newspaper.lower()}_{self.period}_{self.lang}.csv', index=False, encoding='utf-8')

    def dump_tweets(self):
        '''
            return tweets given a specific twitter user and a time interval
            '''
        tweets = []
        df = pd.DataFrame

        try:
            # calls the API to obtain tweets
            # parsing the tweets
            print('scraping tweets...')
            counter = 0
            for i, tw in enumerate(sntwitter.TwitterSearchScraper(
                    f'from:{self.newspaper} since:{self.start} until:{self.end}').get_items()):

                if i > self.n_tweets:

                    df = pd.DataFrame(tweets, columns=(
                        'text', 'date', 'newspaper', 'likes', 'retweets', 'lang', 'period'))
                    print(f'the date of last tweet scraped is {df.date.iloc[-1]}')
                    self.create_csv(df)
                    return df

                else:

                    if counter == self.tweets2sleep:
                        print('i am sleeping')
                        time.sleep(self.sleeping_time)
                        print('scraping tweets...')
                        counter = 0

                    tw_attributes = [tw.content, tw.date, self.newspaper.lower(),
                                     tw.likeCount, tw.retweetCount, self.lang, self.period]
                    tw_attributes_names = ['text', 'date', 'newspaper', 'likes', 'retweets', 'lang', 'period']
                    dic_tweet = {tw_attributes_names[attr]: tw_attributes[attr] for attr in range(len(tw_attributes))}
                    tweets.append(dic_tweet)
                    counter += 1

            df = pd.DataFrame(tweets, columns=('text', 'date', 'newspaper', 'likes', 'retweets', 'lang', 'period'))
            self.create_csv(df)

        except(Exception, KeyboardInterrupt) as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(str(e), fname, exc_tb.tb_lineno)

            try:
                df = pd.DataFrame(tweets, columns=('text', 'date', 'newspaper', 'likes', 'retweets', 'lang', 'period'))
                print(f'the date of last tweet scraped is {df.date.iloc[-1]}')
                self.create_csv(df)
                return df

            except:
                print('No one tweet extracted, dataframe is empty')
                return df

        return df