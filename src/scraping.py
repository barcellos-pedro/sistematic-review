import requests
from bs4 import BeautifulSoup

from src.utils import user_agent

headers = {
    "User-Agent": user_agent
}


def scrape_page(url, raw=True):
    if raw is False:
        return scrape_page_json(url)
    else:
        return scrape_page_raw(url)


def scrape_page_json(url):
    """
    Currently works with pages from: https://ieeexplore.ieee.org
    """

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup.get_text())  # get all content

        # Find the title element
        title_element = soup.find('title')

        # Extract the title text
        title = title_element.text.strip()

        # Find the meta tag containing the abstract/description
        abstract_meta_tag = soup.find('meta', attrs={'name': 'Description'})

        # Extract the abstract/description text
        abstract = abstract_meta_tag['content'].strip()

        return {"title": title, "abstract": abstract}
    else:
        print(f"Error | Status code: {response.status_code}")


def scrape_page_raw(url):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # get source code (ctrl+u in browser)
        return response.text
    else:
        print(f"Error | Status code: {response.status_code}")
