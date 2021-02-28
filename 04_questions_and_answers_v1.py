import csv


# name of csv file goes here...
with open('country-list.csv', 'r') as f:

    # make csv file into list
    file = csv.reader(f)
    my_list = list(file)

print(my_list)
