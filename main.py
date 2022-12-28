from scraping import Tweetscraper
import time

if __name__ == "__main__":

############################################# REPUBBLICA PRECOVID ######################################################

# scraping features

    newspaper = 'repubblica'
    date_start, date_finish = '2019-07-01', '2019-12-31'
    period = 'precovid'
    tweets2sleep = 3200
    sleeping_time_internal = 1800
    sleeping_time_external = 1800
    lang = 'it'

# scraping call

    df_repubblica_precovid = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
                                          period=period, tweets2sleep=tweets2sleep,
                                          sleeping_time=sleeping_time_internal, lang=lang,
                                          path=f'./scraped_tweets/tweets_{period}').dump_tweets()

    print(df_repubblica_precovid.head(5))

# sleeping

    print('to scrape other tweets please wait, i am sleeping')
    time.sleep(sleeping_time_external)

############################################ REPUBBLICA COVID ##########################################################

# # scraping features
#
#     newspaper = 'repubblica'
#     date_start, date_finish = '2020-01-01', '2022-01-31'
#     period = 'covid'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'it'
#
# # scraping call
#
#     df_repubblica_covid = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_repubblica_covid.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################# REPUBBLICA WAR ###########################################################
#
# # scraping features
#
#     newspaper = 'repubblica'
#     date_start, date_finish = '2022-02-01', '2022-05-17'
#     period = 'war'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'it'
#
# # scraping call
#
#     df_repubblica_war = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_repubblica_war.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################ CORRIERE PRECOVID #########################################################
#
# # scraping features
#
#     newspaper = 'Corriere'
#     date_start, date_finish = '2019-07-01', '2019-12-31'
#     period = 'precovid'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'it'
#
# # scraping call
#
#     df_corriere_precovid = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_corriere_precovid.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################# CORRIERE COVID ###########################################################
#
# # scraping features
#
#     newspaper = 'Corriere'
#     date_start, date_finish = '2020-01-01', '2022-01-31'
#     period = 'covid'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'it'
#
# # scraping call
#
#     df_corriere_covid = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_corriere_covid.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################# CORRIERE WAR #############################################################
#
# # scraping features
#
#     newspaper = 'Corriere'
#     date_start, date_finish = '2022-02-01', '2022-05-17'
#     period = 'war'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'it'
#
# # scraping call
#
#     df_corriere_war = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_corriere_war.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################# GIORNALE PRECOVID ########################################################
#
# # scraping features
#
#     newspaper = 'ilgiornale'
#     date_start, date_finish = '2019-07-01', '2019-12-31'
#     period = 'precovid'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'it'
#
# # scraping call
#
#     df_giornale_precovid = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_giornale_precovid.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################# GIORNALE COVID ###########################################################
#
# # scraping features
#
#     newspaper = 'ilgiornale'
#     date_start, date_finish = '2020-01-01', '2022-01-31'
#     period = 'covid'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'it'
#
# # scraping call
#
#     df_giornale_covid = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_giornale_covid.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################# GIORNALE WAR #############################################################
#
# # scraping features
#
#     newspaper = 'ilgiornale'
#     date_start, date_finish = '2022-02-01', '2022-05-17'
#     period = 'war'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'it'
#
# # scraping call
#
#     df_giornale_war = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_giornale_war.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ################################### NYTIMES PRE COVID###################################################################
#
# # scraping features
#
#     newspaper = 'nytimes'
#     date_start, date_finish = '2019-07-01', '2019-12-31'
#     period = 'precovid'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'en'
#
# # scraping call
#
#     df_nytimes_precovid = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_nytimes_precovid.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################ NYTIMES COVID #############################################################
#
# # scraping features
#
#     newspaper = 'nytimes'
#     date_start, date_finish = '2020-01-01', '2022-01-31'
#     period = 'covid'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'en'
#
# # scraping call
#
#     df_nytimes_covid = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_nytimes_covid.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################ NYTIMES WAR ###############################################################
#
# # scraping features
#
#     newspaper = 'nytimes'
#     date_start, date_finish = '2022-02-01', '2022-05-17'
#     period = 'war'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'en'
#
# # scraping call
#
#     df_nytimes_war = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_nytimes_war.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ####################################### WSJ PRE COVID ##################################################################
#
# # scraping features
#
#     newspaper = 'WSJ'
#     date_start, date_finish = '2019-07-01', '2019-12-31'
#     period = 'precovid'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'en'
#
# # scraping call
#
#     df_WSJ_precovid = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_WSJ_precovid.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################# WSJ COVID ################################################################
#
# # scraping features
#
#     newspaper = 'WSJ'
#     date_start, date_finish = '2020-01-01', '2022-01-31'
#     period = 'covid'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'en'
#
# # scraping call
#
#     df_WSJ_covid = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_WSJ_covid.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
#
# ############################################# WSJ WAR ##################################################################
#
# # scraping features
#
#     newspaper = 'WSJ'
#     date_start, date_finish = '2022-02-01', '2022-05-17'
#     period = 'war'
#     tweets2sleep = 3200
#     sleeping_time_internal = 1800
#     sleeping_time_external = 1800
#     lang = 'en'
#
# # scraping call
#
#     df_WSJ_war = Tweetscraper(newspaper=newspaper, start=date_start, end=date_finish,
#                                           period=period, tweets2sleep=tweets2sleep,
#                                           sleeping_time=sleeping_time_internal, lang=lang,
#                                           path=f'./scraped_tweets/tweets_{period}').dump_tweets()
#
#     print(df_WSJ_war.head(5))
#
# # sleeping
#
#     print('to scrape other tweets please wait, i am sleeping')
#     time.sleep(sleeping_time_external)
