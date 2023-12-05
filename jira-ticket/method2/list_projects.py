# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import os
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv

# copy the url link of your jira dashboard upto .net
url = "https://santoshtechguyjira.atlassian.net/rest/api/3/project"

# loading environment from .env file to os.environ()
load_dotenv()

# Accessing JIRA API TOKEN as dictionary
API_TOKEN= os.environ['JIRA_API_TOKEN']

auth = HTTPBasicAuth("santoshtechguy@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
jira_projects_info=json.loads(response.text)
for each_project_info in jira_projects_info:
    print(f'Project Name : {each_project_info["name"]}')
