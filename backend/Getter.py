import snscrape.modules.twitter as apiTwitter
import pandas as pd


'''date_debut = input("Entrez la date de début : ")
date_debut = str(date_debut)
date_fin = input("Entrez la date de fin : ")
date_fin = str(date_fin)
keywords = input("Entrez vos mots clés : ")
limit = input("Entrez le nombre de tweets à récupérer : ")
limit = int(limit)
'''

def get_tweets(keywords, start = None, end = None , num = 100):
    tweets = []
    query = keywords
    if end is not None:
        query += " until:" + end
    if start is not None:
        query += " since:" + start
    # on met la langue par default en anglais car nos modèles ont été entrainés sur des datasets avec des
    # tweets en anglais
    query = str(query + " lang:en")
    for tweet in apiTwitter.TwitterSearchScraper(query).get_items():

        if len(tweets) == num:
            break
        else:
            tweets.append([tweet.date,tweet.user.username,tweet.content])

    tweets_df = pd.DataFrame(tweets,columns=['date','username','tweet'])
    tweets_df['date'] = pd.to_datetime(tweets_df['date'])
    return tweets_df

#print(get_tweets(keywords,date_debut,date_fin,limit))

















'''import re
import csv
import tweepy
import pandas
from tweepy import OAuthHandler
# initialisation de l'API

api_key = 'lWjqhTSQGzMVyFtZIBrrtGxpx'
api_secret = 'tAMosn1FUYOGDuMIlpgtQRTHSQK1cHtRJX8zf0ZcUDeL59IJp7'
access_token = '1507762239247466504-mL7GRwzHjQRk3HAwRzdsun6oEJsth5'
access_token_secret = '4yZc4dwXfKctk3nwnn04P5UHtaG1k3DEUeJEkP19rYrGB'
bear_token = "AAAAAAAAAAAAAAAAAAAAAH4xawEAAAAAfXINd5ttaJboig%2Fz%2Fm5%2FpjPcwlQ%3Dn8dDxtD2KrNwNHoC3wI5DnrjJEy9eJkd33P1MhmkSsBxvwSGVe"

client = tweepy.Client(bearer_token=bear_token)
response = client.search_recent_tweets(query='gana gueye lgbtq+ -is:retweet',max_results = 100)

for tweet in response[0]:
    print("tweet : ",tweet.text)

try:
    # create OAuthHandler object
    auth = tweepy.OAuthHandler(api_key, api_secret)
    # set access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # create tweepy API object to fetch tweets
    api = tweepy.API(auth)
except:
    print("Error: Authentication Failed")

def get_tweets():
    tweets = []

    try:

        fetched_tweets = api.home_timeline()

        return fetched_tweets

    except:

        print("Error : ")

print(get_tweets())
class Listener(tweepy.Stream):
    tweets = []
    limit = 200

    def on_status(self, status):
        self.tweets.append(status)

        if len(self.tweets) == self.limit:
            self.disconnect()

print('3')
stream_tweet = Listener(api_key, api_secret, access_token, access_token_secret)
print('4')
keyword = ['2022', 'python']

tweets = api.home_timeline()
print(tweets)
# def get_tweets(keyword, count = 200):
'''

