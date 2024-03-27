import os

from dotenv import load_dotenv
from openai import OpenAI

from utils import source_code

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)


completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            "role": "system",
            "content": """
                You will be provided with a html page source code.
                I am only interested in the content from it and not some code snippet.
                The html page will be about a scientific research.
                Scrape the page and show me only the research title and the abstract/description.
                I want the result output to be in a csv format, the headers are: title and abstract.
                End each line with a comma starting from the headers.
            """,
        },
        {
            "role": "user",
            "content": source_code
        }
    ]
)

result = completion.choices[0].message.content

print(result)
