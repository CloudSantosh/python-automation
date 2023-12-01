### Creating Jira Ticket using API Token 
Creating a Jira ticket using the Jira REST API with Python involves sending an HTTP POST request to the appropriate endpoint. To authenticate the request, you'll need to use an API token (or username and password, although API tokens are recommended for security reasons). Here's a basic example using the `requests` library in Python:

1. **Install the `requests` library if you haven't already:**
   
    ```bash
    pip install requests
    ```

2. **Write a Python script to create a Jira ticket:**

    ```python
    import requests
    from requests.auth import HTTPBasicAuth
    import access_env_variable

    # Jira API endpoint for creating an issue
    jira_api_url = "https://your-jira-instance/rest/api/2/issue/"

    # Jira username and API token
    jira_username = "your-username"
    api_token = "access the jira api token via import python code access_env_variable"

    # Issue details
    issue_data = {
        "fields": {
            "project": {"key": "YOUR_PROJECT_KEY"},
            "summary": "Issue Summary",
            "description": "Issue Description",
            "issuetype": {"name": "Task"},
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
    ```

    - Replace `"https://your-jira-instance"` with the URL of your Jira instance.
    - Update `"your-username"` and `"your-api-token"` with your Jira username and API token.
    - Set the `"YOUR_PROJECT_KEY"` to the project key where you want to create the issue.
    - Customize the `issue_data` dictionary with the necessary fields for your Jira issue.

3. **Run the script:**

    Save the script in a file, for example, `create_jira_ticket.py`, and run it:

    ```bash
    python create_jira_ticket.py
    ```

    This script will send a POST request to the Jira REST API, creating a new issue based on the provided data.

Make sure to review the Jira REST API documentation for more details on available endpoints and fields: [Jira REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/). Additionally, always ensure that you handle your API tokens securely and follow best practices for authentication.

https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post
