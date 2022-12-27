import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class CountTweetRetweetLike:
    '''
        given a specific newspaper or a group of newspapers, returns the
        graph with the time trend of tweets, retweets and likes of the givens newspaper(s)
                                                                                        '''
    def __init__(self, dataframe, lang, newspaper='all newspapers'):

        self.lang = lang            #language of the newspaper (or newspapers) under analyisis
        self.newspaper = newspaper  #newspaper (or newspapers) under analysis
        self.dataframe = dataframe  #complete dataframe with all tweets of clean_scraped_tweets directory

        months = sorted(list(set([tweet.date for tweet in self.dataframe.itertuples()])))  #months

        #calling methods
        retweets4month = self.count_retweets(months)
        likes4month = self.count_likes(months)
        tweets4month = self.count_tweets(months)

        self.plot_all(months, retweets4month, likes4month, tweets4month)

    def count_retweets(self, months):
        '''
            counts month by month the retweets of the tweets published by a nespaper or a group of newspapers
                                                                                                            '''
        retweets4month = [np.sum([tweet.retweets for tweet in self.dataframe.itertuples()
                                  if (tweet.date == month and tweet.lang == self.lang
                                  and (self.newspaper == tweet.newspaper or self.newspaper == 'all newspapers'))])
                          for month in months]

        return retweets4month

    def count_likes(self, months):
        '''
            counts month by month the likes of the tweets published by a newspaper or a group of newspapers
                                                                                                            '''
        likes4month = [np.sum([tweet.likes for tweet in self.dataframe.itertuples()
                               if (tweet.date == month and tweet.lang == self.lang
                                   and (self.newspaper == tweet.newspaper or self.newspaper == 'all newspapers'))])
                       for month in months]

        return likes4month

    def count_tweets(self, months):
        '''
            counts month by month the tweets published by a newspaper or a group of newspapers
                                                                                            '''
        tweets4month = [np.sum([1 for tweet in self.dataframe.itertuples()
                                if (tweet.date == month and tweet.lang == self.lang
                                    and (self.newspaper == tweet.newspaper or self.newspaper == 'all newspapers'))])
                        for month in months]

        return tweets4month

    def plot_all(self, months, retweets4month, likes4month, tweets4month):
        '''
            plots the graph
                            '''
        # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        # noinspection PyTypeChecker
        fig.add_trace(
            go.Scatter(x=months, y=tweets4month, name="Tweet", mode='lines', line=dict(width=7, color='black'),
                       line_shape='spline'), secondary_y=True)
        # noinspection PyTypeChecker
        fig.add_trace(go.Bar(x=months, y=likes4month, name="Like", marker_color='blue'), secondary_y=False)
        # noinspection PyTypeChecker
        fig.add_trace(go.Bar(x=months, y=retweets4month, name="Retweet", marker_color='orange'),
                      secondary_y=False)

        fig.update_traces(marker_line_color='black', marker_line_width=3)

        # Add figure title
        fig.update_layout(barmode='group', title_text="Trend temporale tweet/like/retweet", title_font_family='Arial',
                          title_x=0.50, title_font_size=23,
                          legend=dict(orientation='h', xanchor="center", x=0.50, y=1))
        # Set x-axis title
        fig.update_xaxes(title_text="Mesi", tickangle=45)
        # Set y-axes titles
        fig.update_yaxes(title_text="Like/Retweet", secondary_y=False)  # left yaxes
        fig.update_yaxes(title_text="Tweet", secondary_y=True)  # right yaxes
        fig.show()








