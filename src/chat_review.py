import os

from dotenv import load_dotenv
from openai import OpenAI

from src.utils import review_prompt

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)


def review_article(article):
    completion = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        max_tokens=10,
        messages=[
            {
                "role": "assistant",
                "content": review_prompt
            },
            {
                "role": "user",
                "content": f"""
                    {article['title']}
                    {article['abstract']}
                """
            }
        ]
    )

    return completion.choices[0].message.content
