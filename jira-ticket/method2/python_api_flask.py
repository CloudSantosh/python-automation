from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

# creating a flask app instance
app=Flask(__name__)

@app.route("/createjira", methods=['POST'])
def createJIRA():
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
                                 "text": "Order entry fails when selecting supplier.",
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
            "summary": "main order flow broken",
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
    app.run(host='0.0.0.0', port=5000)