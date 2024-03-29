import requests

from src.utils import user_agent

headers = {
    "User-Agent": user_agent
}


def scrape_page(url):
    """
    Get page source code (ctrl+u in browser)
    """
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Error on request")
    else:
        return response.text
