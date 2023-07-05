import csv


def write(data):
    with open('repositories.csv', "a") as f:
        writer = csv.writer(f)
        for el in data:
            row = list(el.values())
            writer.writerow(row)

