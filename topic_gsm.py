import gensim
import gensim.corpora as corpora
from pprint import pprint
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
import pyLDAvis
from pyLDAvis.gensim_models import prepare
from bokeh.io import output_notebook
from bokeh.plotting import figure, output_file, save
from tabulate import tabulate
from plotly.subplots import make_subplots
from plotly import graph_objs as go
from sklearn.manifold import TSNE
import os

import warnings


warnings.filterwarnings("ignore")


class TopicGensim:
    '''
        Topic modeling with Gensim library
                                        '''
    def __init__(self, dataframe, period, lang, newspaper='all newspapers'):

        self.dataframe = dataframe    #complete dataframe with all tweets of clean_scraped tweets directory
        self.period = period          #historical period under analysis
        self.lang = lang              #language of the newspaper (or newspapers) under analysis
        self.newspaper = newspaper    #newspaper (or newspapers) under analysis

    def format_topics_sentences(self, ldamodel=None, corpus=None, texts=None):
        '''
            returns a dataframe in which for each topic results the text, the dominant topic,
            the weight of the dominant topic, the top10 words of the dominant topic
                                                                                '''
        # Init output
        sent_topics_df = pd.DataFrame()

        # Get main topic in each document
        for i, row_list in enumerate(ldamodel[corpus]):
            if len(row_list) == 0:
                continue
            row = row_list[0] if ldamodel.per_word_topics else row_list
            if isinstance(row, tuple):
                row = [row]
            row = sorted(row, key=lambda x: (x[1]), reverse=True)
            # Get the Dominant topic, Perc Contribution and Keywords for each document
            for j, (topic_num, prop_topic) in enumerate(row):
                if j == 0:  # => dominant topic
                    wp = ldamodel.show_topic(topic_num)
                    topic_keywords = ", ".join([word for word, prop in wp])
                    sent_topics_df = sent_topics_df.append(
                        pd.Series([int(topic_num), round(prop_topic, 4), topic_keywords]), ignore_index=True)
                else:
                    break
        sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']
        contents = pd.Series(texts)
        sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)

        return sent_topics_df

    def count_dominant_topics(self, df_dominant_topic):
        '''
            prints a table in which each topic number is associated with
            the number of documents in which it is dominant;
            plots a barplot in which each bar is a topic and the height of the bar
            represents the number of documents in which that topic is dominant
                                                                            '''
        n_topics = 4
        topics = [n_topic for n_topic in range(n_topics)]
        topics_with_label = [f'TOPIC{n_topic}' for n_topic in range(n_topics)]
        n_documents = [df_dominant_topic['Dominant_Topic'].value_counts()[topic] for topic in topics]
        dic_count_dominant_topics = {'topics': topics, 'n_documents': n_documents}
        df_count_dominant_topics = pd.DataFrame(dic_count_dominant_topics, columns=['topics', 'n_documents'])

        print(tabulate(df_count_dominant_topics, headers='keys', tablefmt='psql', showindex=False))

        #barplot

        df_count_dominant_topics["Color"] = np.where(df_count_dominant_topics["n_documents"] == max(
            df_count_dominant_topics['n_documents']), 'darkblue', 'darkorange')

        fig = make_subplots()

        fig.add_trace(
            go.Bar(x=topics_with_label, y=df_count_dominant_topics['n_documents'],
                   marker_color=df_count_dominant_topics['Color']))
        fig.update_layout(title_text="Topic Distribution Gensim", title_font_family='Arial',
                            title_x=0.50, title_font_size=23,
                            legend=dict(orientation='h', xanchor="center", x=0.50, y=1))

        fig.update_traces(marker_line_color='black', marker_line_width=3)

        fig.update_xaxes(title_text="Topic", tickangle=0)

        fig.update_yaxes(title_text="N_documents")  # left yaxes
        fig.show()

    def visualize_topics(self, lda_model, corpus):
        '''
            saves the html report topic_visualization to a directory
                                                                    '''
        vis = prepare(lda_model, corpus, dictionary=lda_model.id2word, mds='mmds')
        path = f'./report/report_gensim/{self.period}'
        if not os.path.exists(path): os.makedirs(path)
        pyLDAvis.save_html(vis, f'{path}/topic_visualization_{self.newspaper}_{self.lang}.html')

    def show_topic_clusters(self, lda_model, corpus, n_topics=4):
        '''
            saves html report topic_clusters in a directory
                                                            '''
        topic_weights = []
        for i, row_list in enumerate(lda_model[corpus]):
            topic_weights.append([w for i, w in row_list[0]])

        # Array of topic weights
        arr = pd.DataFrame(topic_weights).fillna(0).values

        # Keep the well separated points (optional)
        arr = arr[np.amax(arr, axis=1) > 0.35]

        # Dominant topic number in each doc
        topic_num = np.argmax(arr, axis=1)

        # tSNE Dimension Reduction
        # t-distributed Stochastic Neighbor Embedding
        tsne_model = TSNE(n_components=2, verbose=1, random_state=0, angle=.99, init='pca')
        tsne_lda = tsne_model.fit_transform(arr)

        # Plot the Topic Clusters using Bokeh
        output_notebook()

        path = f'./report/report_gensim/{self.period}'
        if not os.path.exists(path): os.makedirs(path)
        file_name = f'{path}/topic_clusters_{self.newspaper}_{self.lang}.html'
        output_file(file_name)

        mycolors = np.array([color for name, color in mcolors.TABLEAU_COLORS.items()])
        plot = figure(title="t-SNE Clustering of {} LDA Topics".format(n_topics),
                        plot_width=900, plot_height=700)
        plot.scatter(x=tsne_lda[:, 0], y=tsne_lda[:, 1], color=mycolors[topic_num])
        save(plot)

    def topic_modeling_starter(self):

        documents = [tweet.text.split() for tweet in self.dataframe.itertuples() if (
                tweet.period == self.period and tweet.lang == self.lang and (
                tweet.newspaper == self.newspaper or self.newspaper == 'all newspapers'))]

        id2word = corpora.Dictionary(documents)
        # Create Corpus: Term Document Frequency
        corpus = [id2word.doc2bow(text) for text in documents]
        # Build LDA model
        lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                   id2word=id2word,
                                                   num_topics=4,
                                                   iterations=100,
                                                   decay=0.5,
                                                   random_state=100,
                                                   update_every=1,
                                                   chunksize=10,
                                                   passes=10,
                                                   alpha='symmetric',
                                                   per_word_topics=True)

        pprint(lda_model.print_topics())

        #calling methods
        df_topic_sents_keywords = self.format_topics_sentences(ldamodel=lda_model, corpus=corpus, texts=documents)

        # Format
        df_dominant_topic = df_topic_sents_keywords.reset_index()
        df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']
        print(tabulate(df_dominant_topic.head(15), headers='keys', tablefmt='psql', showindex=False))

        self.count_dominant_topics(df_dominant_topic)

        #Visualize HTML reports of topics and topic clusters
        self.show_topic_clusters(lda_model, corpus, n_topics=4)
        self.visualize_topics(lda_model, corpus)








