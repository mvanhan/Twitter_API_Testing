# OpenAI Key
# sk-proj-GtxgjENr6qvzVoj2Zs0aT3BlbkFJli9Mb5mEYltlwpC1uM11

# Twitter API keys:
# Normal
# SMjfRjncYGvNnVL7Fn6DXD4YE

# Secret
# CncZpvMLJGbjAG0E3aO9DoO5YOFVVIe6B1sKOSkPEIaTdq1F5u

# Access:
# Normal
# 1790767539061915648-eeZHBPxXfm2Cgwj67XqERfUIncGW1u

# Secret
# 6PrB7daMsB3zQvf0all68HzSMKBI9PtKpGR2wBNMJPGr8


import os
import time
import tweepy
import openai

# Set up Twitter API credentials
consumer_key = 'SMjfRjncYGvNnVL7Fn6DXD4YE'
consumer_secret = 'CncZpvMLJGbjAG0E3aO9DoO5YOFVVIe6B1sKOSkPEIaTdq1F5u'
access_token = '1790767539061915648-eeZHBPxXfm2Cgwj67XqERfUIncGW1u'
access_token_secret = '6PrB7daMsB3zQvf0all68HzSMKBI9PtKpGR2wBNMJPGr8'

# Initialize the OpenAI client with your API key
client = openai.OpenAI(
    api_key='sk-proj-GtxgjENr6qvzVoj2Zs0aT3BlbkFJli9Mb5mEYltlwpC1uM11'  # Replace with your actual API key
)

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to generate promotional content
def generate_promotion():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a marketing assistant."},
            {"role": "user", "content": "Create a one-sentence promotional description for a website that is a public poll for the upcoming presidential election. You must include the following link (the link to the website): bidenortrump.org"}
        ]
    )
    return response.choices[0].message.content.strip()

# Function to search tweets based on a keyword
def search(keyword, count=10):
    query = f"{keyword} -is:retweet"  # Avoid retweets
    tweets = api.search_tweets(q=query, count=count, lang='en', result_type='recent')
    return tweets

# Function to comment on tweets
def comment_on_tweets(tweets, link, promotional_content):
    for tweet in tweets:
        try:
            # Posting a reply
            api.update_status(
                text=f"@{tweet.author_id} {promotional_content} {link}",
                in_reply_to_tweet_id=tweet.id
            )
            print(f"Replied to tweet by @{tweet.author_id}")
            time.sleep(10)  # Wait a bit to avoid rate limiting
        except tweepy.TweepError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    keywords = ["politics", "Biden", "Trump", "2024election"]  # List of keywords
    link = "bidenortrump.org"
    promotional_content = generate_promotion()
    
    for keyword in keywords:
        tweets = search(keyword)
        comment_on_tweets(tweets, link, promotional_content)


# import os
# from openai import OpenAI

# client = OpenAI(
#     api_key='sk-proj-GtxgjENr6qvzVoj2Zs0aT3BlbkFJli9Mb5mEYltlwpC1uM11'  
# )

# def generate_text(prompt):
#     try:
#         chat_completion = client.chat.completions.create(
#             model="gpt-3.5-turbo-16k",
#             messages=[
#                 {
#                     "role": "user",
#                     "content": prompt,
#                 }
#             ]
#         )
#         return chat_completion.choices[0].message.content.strip()
#     except Exception as e:
#         return str(e)

# if __name__ == "__main__":
#     prompt = "Who is the current president of the US?"
#     result = generate_text(prompt)
#     print(f"Generated Text: {result}")


