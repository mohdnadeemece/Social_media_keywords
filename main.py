import os
import tweepy

consumer_key = "RGjK2rfqZPx7iMoDPziNIK7j7"
consumer_secret = "jsG3c2gdaDUefVCkJne4UaKEA1R0npmmLnT86KYPCFy8fPRoRT"
access_token = "1753066355027566592-CknHNIgf0U8DS9kxgvB7SGQq4aYqGg"
access_token_secret = "GHe9YlWY1nKZZNQLcpAFyzRYezZgZ6X0wSlbBchzg2Rmu"

# Authentication
auth=tweepy.OAuthHandler(consumer_key, consumer_secret) # identify your app u r not bot
auth.set_access_token(access_token, access_token_secret) # identify your Twitter account.

# API object main tool to talk to Twitter.
api=tweepy.API(auth , wait_on_rate_limit=True)

# Fetch tweets
tweets=api.search_tweets(q="python", count=10, lang="en", tweet_mode='extended')

for tweet in tweets:
    print(f"user:{tweet.user.screen_name}, Tweet: {tweet.text}")
    

#sentiment analysis----------------------------------------------


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

for tweet in tweets:
    sentiment=analyzer.polarity_scores(tweet.text)
    print(f"sentiment: {sentiment["compound"]}, Tweet: {tweet.text} ")




#Visualizing Trends and Engagement----------------------------------

#Collect Engagement Data:

for tweet in tweets:
    retweet_count = tweet.retweet_count
    like_count = tweet.favorite_count
    print(f"Tweet: {tweet.text}, Retweets: {retweet_count}, Likes: {like_count}")
    
#Plot Engagement and Sentiment:

import matplotlib.pyplot as plt

# Sample sentiment and engagement data

sentiments=[-0.5, 0.2, 0.8, -0.1, 0.4]
engagements=[100, 150, 200, 50, 300]

plt.plot(engagements, sentiments,marker='o')
plt.title("Engagement vs sentiment")
plt.xlabel("Enagement (likes/retweets)")
plt.ylabel("sentiment")
plt.show()

#Set Up a Web Interface (Dashboard)

import streamlit as st
import matplotlib.pyplot as plt

# Display title
st.title("Twitter Sentiment Analysis Tool")

# Display tweets

st.subheader("lastest tweets")  

st.write("Here are the latest tweets:")

# Sentiment and engagement plot
st.subheader('Sentiment vs Engagement')
plt.plot(engagements, sentiments, marker='o')
plt.title("Sentiment vs Engagement")
plt.xlabel("Engagement")
plt.ylabel("Sentiment")
st.pyplot()
