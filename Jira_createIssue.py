# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

@app.route('/createIssue')
def Jira_create_issue(userName):

    userName = github_pull_issue()
    url = "https://harshalphadatare.atlassian.net/rest/api/3/issue"

    API_TOKEN = ""
    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "project": {
        "id": "3"
        },
        "reporter": {
        "id": userName['Name']
        },
        "summary": userName['Issue'],
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
    app.run("0.0.0.0", port=5000)