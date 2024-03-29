import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from src.utils import num_tokens, parse_content_prompt

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)


def get_content(content):
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": parse_content_prompt,
            },
            {
                "role": "user",
                "content": content,
            }
        ]
    )

    article = completion.choices[0].message.content
    return json.loads(article)


def parse_content(html, split=True):
    token_limit = 15500

    if num_tokens(html) <= token_limit:
        return get_content(html)

    if num_tokens(html) > token_limit and split == False:
        raise Exception("max tokens reached")

    chunks = []
    article = {"title": "", "abstract": ""}

    while html != "":
        mid = len(html) // 2

        if mid == 0:
            break

        first_part = html[:mid]
        remaining_part = html[mid:]

        html = remaining_part
        result = get_content(first_part)

        if article["title"] == "":
            article["title"] = result["title"]

        if result["abstract"] != "" and 'pdf' not in result["abstract"].lower():
            chunks.append(result["abstract"])

    article["abstract"] = ", ".join(chunks)

    return article
