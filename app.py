import os
from csv import DictReader, DictWriter

from src.chat_review import review_article
from src.chat_scraping import parse_content
from src.scraping import scrape_page

root_dir = os.getcwd()

input_file_path = os.path.join(root_dir, "sample.csv")
output_file_path = os.path.join(root_dir, "result.csv")

fields = ['title', 'url', 'review']

with open(file=input_file_path, mode='r', encoding="utf-8") as csv_input:
    reader = DictReader(csv_input, delimiter=",")

    with open(file=output_file_path, mode="a", encoding='utf-8', newline='') as csv_output:
        writer = DictWriter(csv_output, fieldnames=fields, lineterminator="\n")

        # If output file is empty, write headers
        if os.stat(output_file_path).st_size == 0:
            writer.writeheader()

        # Read file line by line
        for row in reader:
            title, url = row["title"], row["url"]

            if "ieeexplore" not in url:
                continue

            try:
                # Web Scrape
                article_html = scrape_page(url)

                # Extract Title and Abstract from page as JSON
                article_json = parse_content(article_html)

                # Review Content and get result (Yes, No, Maybe)
                review = review_article(article_json)

                # review = review_article(scrape_page(url=url, raw=False))

                # Write to file
                writer.writerow({
                    "title": title,
                    "url": url,
                    "review": review
                })
            except Exception as error:
                print(error, url)
                continue
