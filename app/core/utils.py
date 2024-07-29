import csv
import os

from core.settings import CSVSettings

CSV_DIR = CSVSettings().csv_dir


def save_data_to_csv(data: list[dict], filename="data.csv"):
    with open(os.path.join(CSV_DIR, filename), "w", newline="") as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
