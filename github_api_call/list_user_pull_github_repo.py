import requests


def github_pull_info(response, response_status):
    if response_status==True:
        complete_detail=response.json()
        print("\n*** Listing users login name who Forked this repo ***")
        for every_user_count in range(len(complete_detail)):
            print(complete_detail[every_user_count]['owner']['login'])

    else:
        print(f"Failed to fetch repository information. Status Code: {response.status_code}")
        print(response.text)


def construct_full_url(owner,repo):
    repo_url="https://api.github.com/repos/{owner}/{repo}/forks"
    full_url=repo_url.format(owner=owner, repo=repo)
    print("\n*** Complete URL ***")
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

if __name__ == "__main__":
    owner = input("Enter the Owner Name of GitHub:\n")      # Asking from user to enter owner of Gitub
    repo = input("Enter the repository name to Access:\n")  # Asking from user repository of owner owns
    full_url = construct_full_url(owner, repo)              # Calling function to create full URL based on  github owner and repository
    response = api_request(full_url)                        # Making GitHub API call based on full_url
    response_status = check_response_status(response)       # Checking the status of API call
    github_pull_info(response, response_status)             # making Github pull information based on response status.





