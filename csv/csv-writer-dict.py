import csv

# Data in the form of a list of dictionaries
data = [
    {'Name': 'David', 'Age': 28, 'Location': 'San Francisco'},
    {'Name': 'Eve', 'Age': 22, 'Location': 'Seattle'},
]

# Writing data to a CSV file
with open('new_data.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Name', 'Age', 'Location']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row with field names
    for row in data:
        writer.writerow(row)
