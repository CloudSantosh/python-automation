import os
import csv


# Create a file with data in it
def create_file(filename):
    with open(filename, "w", newline='') as file:  # Use newline='' for consistent line endings
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, "r", newline='') as file:
        # Create a CSV reader
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Process each row
        for row in reader:
            name, color, flower_type = row
            return_string += "a {} {} is {}\n".format(color, name, flower_type)

    return return_string


# Call the function
print(contents_of_file("flowers.csv"))
