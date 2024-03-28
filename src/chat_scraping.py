import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from src.utils import parse_content_prompt, source_code, source_code_pdf

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)


def parse_content(html):
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
                "content": html,
            }
        ]
    )

    result = completion.choices[0].message.content
    return json.loads(result)
