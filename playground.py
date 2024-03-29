import requests

from src.chat_scraping import parse_content
from src.utils import num_tokens, parse_content_prompt, user_agent

url = "https://ieeexplore.ieee.org/document/7896565/"
# url = "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9056993"

headers = {
    "User-Agent": user_agent
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Error | Status code: {response.status_code}")
    exit(1)


html = response.text


def split(text):
    if num_tokens(text) <= 16000:
        return parse_content(text)

    chunks = []

    while text != "":
        mid = len(text) // 2

        if mid == 0:
            break

        first_part = text[:mid]
        remaining_part = text[mid:]

        text = remaining_part
        article = parse_content(first_part)

        if article["abstract"] != "":
            chunks.append(article["abstract"])

    return ", ".join(chunks)


print(num_tokens(html))
print(split(html))
