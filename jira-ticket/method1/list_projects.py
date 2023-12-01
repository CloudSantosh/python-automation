# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import access_env_variable # importing the python code as modules which access the environment variable

# copy the url link of your jira dashboard upto .net
url = "https://santoshtechguyjira.atlassian.net/rest/api/3/project"

# copy paste the Jira API token
API_TOKEN= access_env_variable.jira_api_token

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
#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
jira_projects_info=json.loads(response.text)
for each_project_info in jira_projects_info:
    print(f'Project Name : {each_project_info["name"]}')
