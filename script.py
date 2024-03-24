import os

from dotenv import load_dotenv
from openai import OpenAI

from utils import prompt

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

user_input = """
Uso de exercicios alternando linguagens de programação: Java e Python

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=10,
    messages=[
        {
            "role": "assistant",
            "content": prompt
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
)

result = completion.choices[0].message.content

print(f"Resultado: {result}")  # Yes, No or Maybe
