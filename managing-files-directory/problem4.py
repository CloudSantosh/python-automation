# The parent_directory function returns the name of the directory
# that's located just above the current working directory.
# Remember that '..' is a relative path alias that means "go up to the parent directory".
# Fill in the gaps to complete this function.

import os

def parent_directory():
    # Create a relative path to the parent of the current working directory
    #print(os.pardir)
    #print(os.getcwd())
    relative_parent = os.path.join(os.getcwd(), os.pardir)
    print(relative_parent)

    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)

print(parent_directory())
