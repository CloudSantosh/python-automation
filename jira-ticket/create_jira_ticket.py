# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://santoshtechguyjira.atlassian.net/rest/api/3/issue"

API_TOKEN="ATATT3xFfGF06U0cT1KhLXWwbYwxbeQfelLPpiWs4-esuzqA5A-ulj761yK99-DuSUJ6ghWTU2WBQRoI3JRULQEnHGtZKrccc81jI_fpqmsighgSvi-9bqwwz0MpkwJ5fbLB0NuxFAeKeeCygoaQ3nBaXCcp3d1E5dE7lEiHSZVthfEw5CPUTXM=74563190"

auth = HTTPBasicAuth("santoshtechguy@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "This is first Jira ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10008"
    },

    "project": {
      "key": "TP"
    },
    "summary": "First Jira Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))