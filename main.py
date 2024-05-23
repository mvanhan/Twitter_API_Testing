import os
import time
import tweepy
import openai
from dotenv import load_dotenv


load_dotenv('keys.env')


consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


client = openai.OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')  
)


auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)


def generate_promotion():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a marketing assistant."},
            {"role": "user", "content": "Create a one-sentence promotional description for a website that is a public poll for the upcoming presidential election. You must include the following link (the link to the website): bidenortrump.org"}
        ]
    )
    return response.choices[0].message.content.strip()


def search(keyword, count=10):
    query = f"{keyword} -is:retweet"  # Avoid retweets
    tweets = api.search_tweets(q=query, count=count, lang='en', result_type='recent')
    return tweets


def comment_on_tweets(tweets, link, promotional_content):
    for tweet in tweets:
        try:
            
            api.update_status(
                text=f"@{tweet.author_id} {promotional_content} {link}",
                in_reply_to_tweet_id=tweet.id
            )
            print(f"Replied to tweet by @{tweet.author_id}")
            time.sleep(10)  
        except tweepy.TweepError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    keywords = ["politics", "Biden", "Trump", "2024election"] 
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


