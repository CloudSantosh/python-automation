# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
# copy the url link of your jira dashboard upto .net
url = "https://santoshtechguyjira.atlassian.net/rest/api/3/project"
# copy paste the Jira API token
API_TOKEN="ATATT3xFfGF06U0cT1KhLXWwbYwxbeQfelLPpiWs4-esuzqA5A-ulj761yK99-DuSUJ6ghWTU2WBQRoI3JRULQEnHGtZKrccc81jI_fpqmsighgSvi-9bqwwz0MpkwJ5fbLB0NuxFAeKeeCygoaQ3nBaXCcp3d1E5dE7lEiHSZVthfEw5CPUTXM=74563190"

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
