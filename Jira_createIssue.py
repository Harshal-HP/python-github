import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask
import os
from github_issues import github_pull_issue

app = Flask(__name__)

@app.route('/createIssue', methods=['POST'])
def Jira_create_issue():

    userName = github_pull_issue()
    print(userName)
    url = "https://harshalphadatare.atlassian.net/rest/api/3/issue"

    API_TOKEN = os.getenv("jira_pass")
    EMAIL = os.getenv("jira_email")
    auth = HTTPBasicAuth(EMAIL, API_TOKEN)
    print(auth)
    print(userName['Issue'])
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
        "project": {
           "key": "DEV"
        },
        "issuetype": {
            "id": "10014"
        },
        "summary": f"{userName['Issue']}",
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
    return json.dumps(json.loads(response.text), indent=4)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)