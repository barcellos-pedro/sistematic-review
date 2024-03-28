import os
from csv import DictReader

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "dados.csv")

# Read file
with open(file=file_path, mode='r', encoding="utf-8") as csv_file:
    count = 0

    reader = DictReader(csv_file, delimiter=",")

    for row in reader:
        count += 1
        artigo, url = row["Artigo"], row["URL"]
        print(artigo, url)

    print(f"Processed {count} lines")
