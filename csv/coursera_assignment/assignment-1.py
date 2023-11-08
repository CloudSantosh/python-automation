# For this lab, imagine you are an IT Specialist at a medium-sized company. The Human Resources Department at your
# company wants you to find out how many people are in each department. You need to write a Python script that reads
# a CSV file containing a list of the employees in the organization, counts how many people are in each department,
# and then generates a report using this information. The output of this script will be a plain text file.

import csv

# Function to read and process the CSV file
def count_employees_by_department(csv_filename):
    department_counts = {}

    # Open the CSV file
    with open(csv_filename, 'r') as csv_file:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        reader = csv.DictReader(csv_file, dialect='empDialect')

        for row in reader:
            department = row['Department']
            if department not in department_counts:
                department_counts[department] = 1
            else:
                department_counts[department] += 1
        print(department_counts)

    return department_counts


# Function to generate the report
def generate_report(department_counts, output_filename):
    with open(output_filename, 'w') as report_file:
        report_file.write("Department,Number of Employees\n")
        for department, count in department_counts.items():
            report_file.write(f"{department},{count}\n")


if __name__ == '__main__':
    csv_filename = 'Department_Dataset.csv'  # Replace with the actual CSV filename
    output_filename = 'department_report.txt'  # Replace with the desired output filename

    department_counts = count_employees_by_department(csv_filename)
    generate_report(department_counts, output_filename)

    print(f"Department counts have been saved to '{output_filename}'")
