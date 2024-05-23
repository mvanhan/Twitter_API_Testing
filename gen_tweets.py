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
        # model="gpt-3.5-turbo",
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a marketing assistant."},
            {"role": "user", "content": "Create a creative and engaging tweet promoting a website that is a public poll for the upcoming presidential election. Include the link: bidenortrump.org"}
        ]
    )
    return response.choices[0].message.content.strip()

def post_tweet(content):
    try:
        api.update_status(status=content)
        print("Tweet posted successfully!")
    except tweepy.TweepyException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    link = "bidenortrump.org"
    keywords = ["politics", "Biden", "Trump", "2024election"] 

    tweet_content = generate_promotion()
    api.update_status_with_media(status=tweet_content, filename='./Public Poll PFP.avif')
    
    # post_tweet(tweet_content)
    print("Script execution completed.")
