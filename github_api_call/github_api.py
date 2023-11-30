import requests
import json
# refer https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28
response1=requests.get("https://api.github.com/repos/CloudSantosh/application/pulls")

response2=requests.get("https://api.github.com/repos/CloudSantosh/application/properties/values")

response3=requests.get("https://api.github.com/repos/CloudSantosh/application/commits")
issue=requests.get("https://api.github.com/repos/CloudSantosh/application/secret-scanning/alerts")

print(f'First {response1.json()} Second: {response2.json()} Third: {response3.json()}')

print(f'The issue: {issue.json()}')

# about traffic clone
traffic_clone=requests.get("https://api.github.com/repos/CloudSantosh/application/traffic/clones")
print(f'Traffic clone: {traffic_clone.json()}')

#Get the weekly commit count
count_weekly=requests.get("https://api.github.com/repos/CloudSantosh/python-automation/stats/participation")
print(f'Weekly commits : {count_weekly.json()}')

# Get the hourly commit count for each day
count_hourly=requests.get("https://api.github.com/repos/CloudSantosh/python-automation/stats/punch_card")
print(f'Hourly commit Info : {count_hourly.json()}')


# searching Repositories
repo_search=requests.get("https://api.github.com/search/respositories")
print(f'Repository Information : {repo_search.json()}')
