from openai import OpenAI
from config import Config

client=OpenAI(
    api_key=Config.GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def chat(user_query:str)->str:
    response=client.chat.completions.create(
        model="gemma-4-31b-it",
        messages=[
            {
                "role":"user",
                "content":user_query
            }
        ]
    )

    ai_response=response.choices[0].message.content

    if "</thought>" in ai_response:
        ai_response=ai_response.split("</thought>")[1]

    return ai_response