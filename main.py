import openai
from openai import OpenAI

def chatbot(message):
    base_url = "https://api.aimlapi.com/v1"
    api_key = "43cca4d19363433f8fac5325ad0745e6"
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
    