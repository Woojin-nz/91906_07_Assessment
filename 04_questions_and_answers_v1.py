import csv

with open("country-list.csv", newline="") as f:
    reader = csv.reader(f)

    next(reader)

    capital_list = [tuple(row) for row in reader]

print(capital_list)
