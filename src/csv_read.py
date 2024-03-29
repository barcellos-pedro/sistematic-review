import os
from csv import DictReader

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "sample.csv")

# Read file
with open(file=file_path, mode='r', encoding="utf-8") as csv_file:
    count = 0

    reader = DictReader(csv_file, delimiter=",")

    for row in reader:
        count += 1
        c1, c2 = row["title"], row["url"]
        print(c1, c2)

    print(f"Processed {count} lines")
