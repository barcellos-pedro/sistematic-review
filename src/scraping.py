import requests
from bs4 import BeautifulSoup

url = "https://ieeexplore.ieee.org/document/9056993"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # print(response.text) # all html content
    # print(soup.get_text()) # all content

    title_tag = soup.find('title')
    title = title_tag.text if title_tag else "Title not found"

    description_tag = soup.find('meta', attrs={'property': 'og:description'})
    description = description_tag['content'] if description_tag else "Description not found"

    print(f"[Title]\n{title}")
    print(f"[Description]\n {description}")

else:
    print(f"Failed to get page. Status code: {response.status_code}")
