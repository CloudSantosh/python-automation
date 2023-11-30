import requests

def github_pull(owner, repo)
    response  = requests.get(f"https://api.github.com/repos/{owner}/{repo}/pulls")
    pass


