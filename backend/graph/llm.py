from openai import OpenAI
from backend.config import Config

ai_client=OpenAI(
    api_key=Config.GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def chat(user_query:str)->str:
    response=ai_client.chat.completions.create(
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