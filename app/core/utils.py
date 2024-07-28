import csv
import os

from core.settings import CSVSettings

CSV_DIR = CSVSettings().csv_dir


def save_data_to_csv(data: dict, filename="data.csv"):
    with open(os.path.join(CSV_DIR, filename), "w", newline="") as csvfile:
        fieldnames = data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
