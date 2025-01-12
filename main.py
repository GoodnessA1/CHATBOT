import openai
from openai import OpenAI
import os

def chatbot(message):
    base_url = "https://api.aimlapi.com/v1"
    api_key = os.getenv('API_KEY')
    api = OpenAI(base_url=base_url, api_key=api_key)

    completion = api.chat.completions.create(
        model= 'gpt-4o',
        messages= [
            {
                "role": "system",
                "content": "You are a helpful assistant that chats with people generally to keep them company",
            },
            {
                "role": "user",
                "content": message,
            }
        ],
        temperature=0.7,
        max_tokens=256,
    )
    
    response = completion.choices[0].message.content
    return response
    