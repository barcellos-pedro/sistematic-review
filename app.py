import os
import time
from csv import DictReader, DictWriter

import openai

from src.chat_review import review_article
from src.chat_scraping import parse_content
from src.scraping import scrape_page

root_dir = os.getcwd()

input_file_path = os.path.join(root_dir, "pendentes.csv")
output_file_path = os.path.join(root_dir, "resultado.csv")

start = time.time()
count = 0
errors = 0

print("🤖 Start review")

with open(file=input_file_path, mode='r', encoding="utf-8") as csv_input:
    reader = DictReader(csv_input, delimiter=",")

    # Read file line by line
    for row in reader:
        with open(file=output_file_path, mode="a", encoding='utf-8', newline='') as csv_output:
            writer = DictWriter(
                csv_output,
                fieldnames=['title', 'url', 'review', 'error'],
                lineterminator="\n"
            )

            # If output file is empty, write headers
            if os.stat(output_file_path).st_size == 0:
                writer.writeheader()

            title, url = row["title"], row["url"]

            try:
                # Web Scrape
                article_html = scrape_page(url)

                # Extract Title and Abstract from page as JSON
                article_json = parse_content(article_html)

                # Review Content and get result (Yes, No, Maybe)
                review = review_article(article_json)

                # Write to file
                writer.writerow({
                    "title": title,
                    "url": url,
                    "review": review,
                    "error": "no"
                })
            except openai.RateLimitError as e:
                print(f"OpenAI API request exceeded rate limit: {e}")

                end = time.time()
                bench = end - start

                print("\n✅ Review done")
                print(f"{count} files. {errors} errors.")
                print(f"⏱️ Elapsed time: {bench:.2f}")

                exit(1)
            except Exception as error:
                errors += 1

                writer.writerow({
                    "title": title,
                    "url": url,
                    "review": "",
                    "error": "yes"
                })
            finally:
                count += 1
                print(count, end=" ")


end = time.time()
bench = end - start

print("\n✅ Review done")
print(f"{count} files. {errors} errors.")
print(f"⏱️ Elapsed time: {bench:.2f}")
