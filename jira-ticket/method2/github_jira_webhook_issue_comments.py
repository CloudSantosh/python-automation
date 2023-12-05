from flask import Flask, request, jsonify
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os
import requests

# Creating a Flask app instance
app = Flask(__name__)


# Endpoint for GitHub Webhook
@app.route("/github_webhook", methods=['POST'])
def github_webhook():
    # Load environment variables
    load_dotenv()

    # Parse the incoming JSON payload
    payload = request.json

    # Check if the payload is an issue comment event
    if 'issue' in payload and 'comment' in payload:
        issue_comment = payload['comment']['body']

        # Specify the keywords to trigger Jira creation
        keywords = ['/jira', '/Jira', '/JIRA']

        # Check if any of the keywords is present in the issue comment
        if any(keyword in issue_comment for keyword in keywords):
            create_jira_issue()

    return jsonify({'message': 'Webhook received successfully'}), 200


def create_jira_issue():
    url = "https://santoshtechguyjira.atlassian.net/rest/api/3/issue"

    # Accessing API token from hidden .env
    api_token = os.environ['JIRA_API_TOKEN']

    # Making HTTPbasic authentication
    auth = HTTPBasicAuth("santoshtechguy@gmail.com", api_token)

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
                                "text": "Jira ticket with correspond text has been created",
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
            "summary": "Jira Ticket",
        },
        "update": {}
    })

    response = requests.request(
        "POST",
        url,
        json=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == "__main__":
    app.run('0.0.0.0')
