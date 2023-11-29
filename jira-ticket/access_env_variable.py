import os

def load_environment_variables(file_path):
    with open(file_path, "r") as file:
        for line in file:
            # Strip whitespace and split the line into key-value pairs
            key, value = map(str.strip, line.split('=', 1))
            os.environ[key] = value

# Specify the path to your environment variables file
# user needs to create directory name environment_variable and create hidden  file  as .env and store token
file_path = "./environment_variables/.env"

# Load environment variables from the file
load_environment_variables(file_path)

# Example: Access environment variables
jira_api_token = os.environ.get("JIRA_API_TOKEN")
#database_url = os.environ.get("DATABASE_URL")

#print("Jira API Token:", jira_api_token)
#print("Database URL:", database_url)