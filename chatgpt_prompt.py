import os
from openai import OpenAI
import openai
from dotenv import load_dotenv


load_dotenv('keys.env')

client = openai.OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')  
)

def generate_text(prompt):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    prompt = "Who is the current president of the US?"
    result = generate_text(prompt)
    print(f"Generated Text: {result}")
