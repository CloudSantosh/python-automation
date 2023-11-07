import csv

# Data to be written to the CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Specify the file name
csv_file = "example.csv"

# Create and open the CSV file in write mode
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)  # Create a CSV writer object

    # Write the data to the CSV file
    writer.writerows(data)

print(f"CSV file '{csv_file}' has been created with the data.")
