import requests
from requests.auth import HTTPBasicAuth

# Jira API endpoint for creating an issue
jira_api_url = "https://santoshtechguyjira.atlassian.net/rest/api/2/issue/"

# Jira username and API token
jira_username = "santoshtechguy@gmail.com"
api_token = "ATATT3xFfGF06U0cT1KhLXWwbYwxbeQfelLPpiWs4-esuzqA5A-ulj761yK99-DuSUJ6ghWTU2WBQRoI3JRULQEnHGtZKrccc81jI_fpqmsighgSvi-9bqwwz0MpkwJ5fbLB0NuxFAeKeeCygoaQ3nBaXCcp3d1E5dE7lEiHSZVthfEw5CPUTXM=74563190"

# Issue details
issue_data = {
    "fields": {
        "project": {"key": "TP"},
        "summary": "Second jira Ticket",
        "description": "Issue Description",
        "issuetype": {"id": "10008"},
        # Add any other necessary fields here
    }
}

# Headers for the request
headers = {
    "Content-Type": "application/json",
}

# Authentication using API token
auth = HTTPBasicAuth(jira_username, api_token)

# Make the API request to create the issue
response = requests.post(jira_api_url, json=issue_data, headers=headers, auth=auth)

# Check the response status
if response.status_code == 201:
    print("Jira issue created successfully.")
else:
    print(f"Failed to create Jira issue. Status code: {response.status_code}")
    print(response.text)
