import os
# define the file path and name
file_path="test.txt"

#check if the file already exits

if(os.path.exists(file_path)):
    print(f'The file {file_path} already exist and it is renaming')
    os.rename('test.txt', 'testing.txt')
else:
    print(f'The file {file_path} does not exist so we are creating')
    with open(file_path,'w') as file:
        file.write("this is test file")
