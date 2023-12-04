from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

# creating a flask app instance
app = Flask(__name__)

@app.route("/github-webhook", methods=['POST'])
def github_webhook():
    # Ensure that the request is a JSON payload
    if request.headers['Content-Type'] == 'application/json':
        payload = request.json

        # Check for the specific GitHub event (e.g., push event)
        if 'push' in payload.get('event', ''):
            # Check for specific keywords in the commit message
            if 'your_keyword' in [commit.get('message', '') for commit in payload.get('commits', [])]:
                create_jira_ticket()

    return "Webhook received successfully", 200

def create_jira_ticket():
    url = "https://santoshtechguyjira.atlassian.net/rest/api/3/issue"

    # This line brings all environment variables from .env into os.environ
    load_dotenv()

    # Accessing API token from hidden .env
    API_TOKEN = os.environ['JIRA_API_TOKEN']

    # Making HTTPbasic authentication
    auth = HTTPBasicAuth("santoshtechguy@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
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
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
