import csv


def save_data_to_csv(data: dict, filename="data.csv"):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
