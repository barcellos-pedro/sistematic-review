import csv

with open(file="dados.csv", mode='r', encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=",")

    count = 0

    for row in reader:
        article = row["Artigo"]
        url = row["URL"]

        print(f"Titulo: {article[:15]}... | URL: {url[12:-10]}...")

        count += 1

    print(f"Processed {count} lines")
