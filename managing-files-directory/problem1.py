#The create_python_script function creates a new python script in the current working directory
# and adds lines of comments to it declared by the "comments" variables
# and returns the size of the new file

import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename,"a") as file:
    file.write(comments)
    print(f'The size of the file is {os.path.getsize(filename)}')
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))