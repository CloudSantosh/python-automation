import requests
import os
from dotenv import load_dotenv

# This line brings all environment variables from .env into os.environ
load_dotenv()

# The load_dotenv function brings environment variables from the .env file into os.environ, which can then be used like
# any other environment variables set by your operating system.

#print(os.getenv('OWNER'))
#print(os.getenv('REPO'))

print(os.environ['OWNER'])
print(os.environ['REPO'])


# GitHub API endpoint for a public repository
repo_url = "https://api.github.com/repos/{owner}/{repo}"

# Replace {owner} and {repo} with the actual owner and repository name
owner = os.getenv('OWNER')
repo = os.getenv('REPO')

# Construct the full URL
full_url = repo_url.format(owner=owner, repo=repo)

# Make the API request
response = requests.get(full_url)

# Check the response status
if response.status_code == 200:
    # The request was successful, print some information from the response
    repo_data = response.json()
    print(f"Repository Name: {repo_data['name']}")
    print(f"Description: {repo_data['description']}")
    print(f"URL: {repo_data['html_url']}")
else:
    print(f"Failed to fetch repository information. Status code: {response.status_code}")
    print(response.text)
