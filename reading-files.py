import os

print(f'The size of the file is {os.path.getsize("Life Expectancy at Birth.csv")}')
with open("Life Expectancy at Birth.csv", 'r') as file:
    for eachline in file:
        print(eachline)

