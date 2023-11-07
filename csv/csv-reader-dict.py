import csv

# Reading a CSV file into a list of dictionaries
data = []
with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)
for info in data:
    print(info)

# Accessing data
for row in data:
    print(row['Name'], row['Age'], row['Location'])
