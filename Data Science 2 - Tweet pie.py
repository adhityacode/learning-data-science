# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:21:04 2017

@author: Reza
"""

import tweepy
from textblob import TextBlob
0
consumer_key = "FCCQNuHGkX21fPcSDVhJXulin"
consumer_secret = "voA5GoD9k2UQTYIaLNYaW2eEQTo1iCfz11iJcQ4BX3SzVEHm8n"

access_token = "41799075-4uktfujaReiNmn4mk2VunlDeojYYCn4JKSmMc66Ud"
access_token_secret = "VN5VTDbiNsYgrYdn87eTSkMVNwMTpFl66MXuNbOj5Myxh"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Obama')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print analysis.sentiment

'''
wiki = TextBlob("Siraj is angry that he never gets good matches on Tinder")
print wiki.tags
'''