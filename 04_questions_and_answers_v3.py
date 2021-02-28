import pandas

colnames = ["Country", "Capital"]
data = pandas.read_csv("country-list.csv", names=colnames)

print(data)
