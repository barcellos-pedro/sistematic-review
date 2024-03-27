import os
from csv import DictWriter

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "dados.csv")

fields = ["Artigo", "URL"]

# Write file
with open(file=file_path, mode='a', newline="", encoding="utf-8") as csv_file:
    writer = DictWriter(csv_file, fieldnames=fields, lineterminator="\n")

    # writer.writeheader()

    writer.writerow({
        "Artigo": "Test",
        "URL": "http://localhost"
    })
