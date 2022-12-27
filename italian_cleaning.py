import pandas as pd
import os
import spacy
import re
from spacy.lang.it.stop_words import STOP_WORDS
import numpy as np


class ItalianCleaner:
    '''
        allows to pre-process and clean tweets from a dataframe containing dirty italian tweets
        returns a csv file with cleaned tweets
                                            '''
    def __init__(self, dataframe, path, file_name):

        self.dataframe = dataframe  #dataframe obtained by dirty csv file
        self.path = path            #csv file path
        self.file_name = file_name  #csv file name

    def pipeline(self):
        '''
            calls step by step the methods that allows to pre-process your tweets
            and to save them first in a dataframe and then in a new csv file
                                                                            '''
        nlp = spacy.load("it_core_news_md")

        final_tweets_texts = []
        tweets_texts = [tweet.text for tweet in self.dataframe.itertuples()]
        tweets_texts_cleaned = [self.clean_rubbish(tw) for tw in tweets_texts]

        for tweet_text_cleaned in nlp.pipe(tweets_texts_cleaned, disable=['parser', 'ner', 'textcat']): #tokenization
            tweet_text_no_stop = self.stop(tweet_text_cleaned)
            tweet_text_final = self.lemma(tweet_text_no_stop)
            final_tweets_texts.append(tweet_text_final)

        clean1_dataframe = self.update_df(final_tweets_texts)
        clean2_dataframe = self.remove_duplicates(clean1_dataframe)
        clean3_dataframe = self.remove_empty_texts(clean2_dataframe)
        clean4_dataframe = self.datetime_format(clean3_dataframe)

        self.create_clean_csv(clean4_dataframe)

    def clean_rubbish(self, text):
        '''
            cleans raw text from: all special characters; alone numbers;
            square brackets, curly brackets and the words inside them
                                                                    '''
        text = re.sub('’', "'", text)
        text_no_brackets = (re.sub("[{\[].*?[}\]]", "", text))
        text_no_alone_num = (re.sub("\\b[0-9]+\\b", "", text_no_brackets))
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-zÀ-ú'’ \t])|(https?\S+)|(_)", " ", text_no_alone_num).split())

    def stop(self, tweet_text_cleaned):
        '''
            cleans tokenized text from: stopwords; apostrophized_words; italian_trash_words
                                                                                            '''
        apostrophized_words = ["qual'", "nell'", "all'", "nient'", "cos'", "com'", "dov'", "quant'", "quand'",
                               "nessun'", "un'", "dell'", "grand'", "quell'", "sull'", "quest'", "mezz'", "senz'",
                               "tutt'", "anch'", "c'", "d'", "s'", "v'", "t'", "m'", "l'", "po'", "di'", "fa'", "va'",
                               "sta'", "da'", "null'"]

        italian_trash_words = ["null", "rep", "o", "si", "de", "mi", "ti", "vi", "ci", "li", "lo", "la", "ne", "sì",
                               "repubblica", "corriere", "giornale", "rt", "volere", "potere", "sapere", "arrivare",
                               "dovere"]

        tweet_nostop = [t for t in tweet_text_cleaned if
                        (not t.is_punct and not t.is_stop and not t.text.lower() in apostrophized_words and
                         not t.text.lower() in italian_trash_words)]
        return tweet_nostop

    def lemma(self, tweet_nostop):
        '''
            lemmatizes words, removes: stopwords and italian trash words once more after lemmatization;
            removes words with lenght 1
                                        '''
        italian_trash_words = ["null", "rep", "o", "si", "de", "mi", "ti", "vi", "ci", "li", "lo", "la", "ne", "sì",
                               "repubblica", "corriere", "giornale", "rt", "volere", "potere", "sapere",
                               "arrivare", "dovere"]

        tweet_lemmatized_unstopped_ = [t.lemma_.lower() for t in tweet_nostop]
        tweet_text_final_trash = " ".join(tweet_lemmatized_unstopped_)
        tweet_text_final_splitted_trash = tweet_text_final_trash.split()
        tweet_text_final_splitted_no_trash = [word for word in tweet_text_final_splitted_trash if (
                word not in STOP_WORDS and word not in italian_trash_words and len(word) > 1)]
        tweet_text_final = " ".join(tweet_text_final_splitted_no_trash)
        return tweet_text_final

    def update_df(self, final_tweets_texts):
        '''
            updates with clean text the 'text' column of the dataframe obtained by old and dirty csv file
                                                                                                        '''
        self.dataframe.text = final_tweets_texts
        return self.dataframe

    def remove_duplicates(self, dataframe):
        '''
            from dataframe removes duplicated tweets
                                                    '''
        dataframe.drop_duplicates(subset='text', keep='first', ignore_index=True, inplace=True)
        return dataframe

    def remove_empty_texts(self, dataframe):
        '''
            from dataframe removes tweets left with no text after pre-processing
                                                                                '''
        dataframe['text'].replace('', np.nan, inplace=True)
        dataframe.dropna(subset=['text'], inplace=True)
        dataframe.reset_index(drop=True, inplace=True)
        return dataframe

    def datetime_format(self, dataframe):
        '''
            from tweets dates removes: jetlegs, days, hours, minutes, seconds
                                                                            '''
        dataframe['date'] = pd.to_datetime(dataframe.date).dt.strftime("%Y-%m")
        return dataframe

    def create_clean_csv(self, dataframe):
        '''
            from dataframe creates a new csv file with clean tweets
                                                                    '''
        path = f'clean_{self.path}'
        if not os.path.exists(path): os.makedirs(path)
        dataframe.to_csv(f'{path}\\{self.file_name}', index=False, encoding='utf-8')


