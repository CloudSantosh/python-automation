
# The file_date function creates a new file in the current working directory, checks the date that the file was modified,
# and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a
# file called "newfile.txt" and check the date that it was modified.

import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w') as file:
        pass  # This creates an empty file

    # Get the timestamp when the file was last modified
    timestamp = os.path.getmtime(filename)

    # Convert the timestamp into a readable format and then into a string
    date = datetime.datetime.fromtimestamp(timestamp).date()
    date_str = date.strftime("%Y-%m-%d")

    # Return just the date portion
    return date_str

print(file_date("newfile.txt"))
