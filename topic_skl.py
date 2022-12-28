import os
import pandas as pd
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from tabulate import tabulate
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class TopicScikit:
    '''
        Topic modeling with Scikit-learn library
                                                '''
    def __init__(self, dataframe, period, lang, newspaper='all newspapers'):

        self.dataframe = dataframe    #complete dataframe with all tweets of clean_scraped tweets directory
        self.period = period          #historical period under analysis
        self.lang = lang              #language of the newspaper (or newspapers) under analysis
        self.newspaper = newspaper    #newspaper (or newspapers) under analysis

    def color_green(self, val):
        color = 'green' if val > .1 else 'black'
        return 'color: {col}'.format(col=color)

    def make_bold(self, val):
        weight = 700 if val > .1 else 400
        return 'font-weight: {weight}'.format(weight=weight)

        ###############################################################################

    def report_tweets_dominant_topic(self, documents, ldaData, topics, tf_feature_names):
        '''
            creates and saves an html report in which for each document its text and its dominant topic are shown;
            for the dominant are then shown its weight and its 10topwords;
            the content of the html report is also printed
                                                        '''
        print('REPORT TWEETS DOMINANT TOPIC')
        list_dicts = []
        for n_doc in range(0, len(documents)):
            doc_text = " ".join(documents[n_doc])
            doc_topics = ldaData[n_doc]

            # the dominant topic is the one with the highest value, argmax return the index of max in a numpy array
            doc_dominant_topic = np.array(doc_topics).argmax()
            weight_dominant_topic = max(doc_topics)
            # again top 10 words for the dominant topic of doc0
            top10_topic_word_indexes_of_doc = topics[doc_dominant_topic].argsort()[:-11:-1]
            top10_words_of_doc = " ".join(
                [tf_feature_names[wordIndex] for wordIndex in top10_topic_word_indexes_of_doc])
            list_dicts.append(
                {'text': doc_text, 'topic': doc_dominant_topic, 'weight': weight_dominant_topic,
                 'top words': top10_words_of_doc})

        df = pd.DataFrame(list_dicts)
        df.index = ['Doc %d' % i for i in range(len(documents))]
        df_style = df.head(15).style
        path = f'./report/report_scikit/{self.period}'
        if not os.path.exists(path): os.makedirs(path)
        with open(f'{path}/ldaReport2_{self.newspaper}_{self.lang}.html', 'w') as fileWriter:
            fileWriter.write(df_style.render())
        print(tabulate(df.head(15), headers='keys', tablefmt='psql'))

    def dominant_topic_report(self, topics, ldaTransformedDate, numberOfDocuments):
        '''
            prints a table showing for each document: the various topics with the relative weights in the document;
            the dominant topic of the document
                                            '''
        # column names
        topicnames = ["Topic" + str(i) for i in range(topics)]
        # index names
        docnames = ["Doc" + str(i) for i in range(numberOfDocuments)]
        # Make the pandas dataframe
        df_document_topic = pd.DataFrame(np.round(ldaTransformedDate, 2),
                                         columns=topicnames,
                                         index=docnames)

        dominantTopic = np.argmax(df_document_topic.values,
                                  axis=1)
        df_document_topic['dominant_topic'] = dominantTopic
        # Apply Style
        df_document_topics = df_document_topic.head(100).style.applymap(self.color_green).applymap(self.make_bold)
        path = f'./report/report_scikit/{self.period}'
        if not os.path.exists(path): os.makedirs(path)
        with open(f'{path}/ldaReport_{self.newspaper}_{self.lang}.html', 'w') as fileWriter:
            fileWriter.write(df_document_topics.render())
        print(tabulate(df_document_topic.head(15), headers='keys', tablefmt='psql'))
        return df_document_topic

    def topic_distribution(self, df_document_topic_frame):
        '''
            prints a table in which each topic number is associated with
             the number of documents in which it is dominant
                                                            '''
        df_topic_distribution = df_document_topic_frame['dominant_topic'].value_counts().reset_index(
            name="Num Documents")
        df_topic_distribution.columns = ['TopicNum', 'NumDocuments']
        print(tabulate(df_topic_distribution, headers='keys', tablefmt='psql', showindex=False))
        return df_topic_distribution

    def make_topic_distribution_plot(self, df_topic):
        '''
            plots a barplot in which each bar is a topic and the height of the bar
            represents the number of documents in which that topic is dominant
                                                                            '''
        df_topic["Color"] = np.where(df_topic["NumDocuments"] == max(df_topic['NumDocuments']), 'darkblue',
                                     'darkorange')
        topics = [f'TOPIC {topic.TopicNum}' for topic in df_topic.itertuples()]

        fig = make_subplots()
        fig.add_trace(go.Bar(x=topics, y=df_topic['NumDocuments'], marker_color=df_topic['Color']))
        fig.update_layout(title_text="Topic Distribution Scikit", title_font_family='Arial',
                          title_x=0.50, title_font_size=23,
                          legend=dict(orientation='h', xanchor="center", x=0.50, y=1))

        fig.update_traces(marker_line_color='black', marker_line_width=3)

        fig.update_xaxes(title_text="Topic", tickangle=0)

        fig.update_yaxes(title_text="N_documents")  # left yaxes
        fig.show()

    def report_topic_key_words(self, topics, featureNames, topWords=10):
        '''
            prints a table in which for each topic  the 10 topwords
             of that topic are printed with the relative weights
                                                                '''
        keywords = np.array(featureNames)
        topic_keywords = []
        for topicWeights in topics:
            topKeyWordIndexesAndWeights = []
            topKeywordDocs = topicWeights.argsort()[:-1 - topWords:-1]
            pesi = sorted(topicWeights, reverse=True)
            for i in range(0, len(topKeywordDocs)):
                topKeyWordIndexesAndWeights.append((topKeywordDocs[i], round(pesi[i], 2)))
            topKeywordsAndWeights = [(keywords.take(wordindex_weight[0]), wordindex_weight[1]) for wordindex_weight
                                     in topKeyWordIndexesAndWeights]
            topKeyWordsWithWeights = [f'{word_weight[0]},{word_weight[1]}' for word_weight in
                                      topKeywordsAndWeights]

            topic_keywords.append(topKeyWordsWithWeights)

        df_topic_keywords = pd.DataFrame(topic_keywords)

        df_topic_keywords.columns = ['Word %d' % i for i in range(df_topic_keywords.shape[1])]
        df_topic_keywords.index = ['Topic %d' % i for i in range(df_topic_keywords.shape[0])]
        print(tabulate(df_topic_keywords, headers='keys', tablefmt='psql'))

    def update_parameters(self, grid_lda):
        '''
            writes to a txt file the best parameters returned by the topic modeling
                                                                                '''
        openfile = open(f'./topic_parameters/{self.period}_{self.newspaper}_parameters.txt', 'w')
        openfile.write(f'best parameters are: {grid_lda.best_params_}')
        openfile.close()

    def ghost_tokenizer(self, doc):
        '''
            allows to avoid tokenization and pre-processing
                                                            '''
        return doc

    def topic_modeling_starter(self):

        #passing the documents
        documents = [tweet.text.split() for tweet in self.dataframe.itertuples() if (
                tweet.period == self.period and tweet.lang == self.lang and (
                tweet.newspaper == self.newspaper or self.newspaper == 'all newspapers'))]

        tf_vectorizer = CountVectorizer(tokenizer=self.ghost_tokenizer,
                                        preprocessor=self.ghost_tokenizer,
                                        max_df=0.80, max_features=1500
                                        )
        data_vectorized = tf_vectorizer.fit(documents)
        data_vectorized = tf_vectorizer.transform(documents)
        tf_feature_names = tf_vectorizer.get_feature_names_out()

        #LDA
        lda = LatentDirichletAllocation(learning_method='online')
        search_params = {'n_components': [n for n in range(4, 10)],
                         'learning_decay': [.5, .7, .9], 'max_iter': [50, 75, 100]}
        grid_lda = GridSearchCV(lda, param_grid=search_params)

        # Best Model
        grid_lda.fit(data_vectorized)
        ldaBestModel = grid_lda.best_estimator_
        ldaData = ldaBestModel.transform(data_vectorized)
        topics = len(ldaBestModel.components_)
        print(ldaBestModel.components_, 'best model')

        # Model Parameters
        print("Best Model's Params: %s" % grid_lda.best_params_)
        # Log Likelihood Score
        print("Best Log Likelihood Score: %.3f" % grid_lda.best_score_)
        # Perplexity
        print("Model Perplexity: %.3f" % ldaBestModel.perplexity(data_vectorized))

        #calling methods
        df_document_topics = self.dominant_topic_report(topics,
                                                ldaData,
                                                len(documents))

        df_topic_distribution = self.topic_distribution(df_document_topics)

        self.make_topic_distribution_plot(df_topic_distribution)

        self.report_topic_key_words(ldaBestModel.components_,
                                                    tf_vectorizer.get_feature_names_out())

        self.report_tweets_dominant_topic(
            documents, ldaData, ldaBestModel.components_, tf_feature_names)

        self.update_parameters(grid_lda)









