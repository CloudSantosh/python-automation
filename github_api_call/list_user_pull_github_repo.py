import requests


def github_pull_info(response, response_status):
    if response_status==True:
        complete_detail=response.json()
        for every_user_count in range(len(complete_detail)):
            print(complete_detail[every_user_count]['user']['login'])

    else:
        print(f"Failed to fetch repository information. Status Code: {response.status_code}")
        print(response.text)


def construct_full_url(owner,repo):
    repo_url="https://api.github.com/repos/{owner}/{repo}/pulls"
    full_url=repo_url.format(owner=owner, repo=repo)
    print(full_url)
    return full_url

def api_request(full_url):
    response=requests.get(full_url)
    return response

def check_response_status(response):
    if response.status_code==200:
        return True
    else:
        return False

# Asking from user to enter owner of Gitub
owner=input("Enter the Owner Name of GitHub:\n")

# Asking from user repository of owner owns
repo=input("Enter the repository name to Access:\n")

# Calling function to construct full URL on the basis of github owner and repository entered by users
full_url=construct_full_url(owner, repo)

# Making GitHub API call based on full_url
response=api_request(full_url)

#Checking the status of API call
response_status=check_response_status(response)

# making Github pull information based on response status.
github_pull_info(response, response_status)






