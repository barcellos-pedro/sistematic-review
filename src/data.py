import os
from csv import DictReader, DictWriter

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "dados.csv")

# Write file
with open(file=file_path, mode='a', newline="", encoding="utf-8") as csv_file:
    fields = ["Artigo", "URL"]
    writer = DictWriter(csv_file, fieldnames=fields, lineterminator="\n")

    writer.writerow({"Artigo": "Test", "URL": "http://localhost"})


# Read file
with open(file=file_path, mode='r+', encoding="utf-8") as csv_file:
    count = 0

    reader = DictReader(csv_file, delimiter=",")

    for row in reader:
        count += 1

        article = row["Artigo"]
        url = row["URL"]
        print(f"Titulo: {article[:15]}... | URL: {url[12:-10]}...")

    print(f"Processed {count} lines")
