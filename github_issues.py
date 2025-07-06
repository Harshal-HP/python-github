import requests
import json

userName = {}

def github_pull_issue():
    response = requests.get(f"https://api.github.com/repos/Harshal-HP/python-github/issues")

    if response.status_code == 200:
        response_data = response.json()
        for data in response_data:
            for mapData in data.items():
                userName['number']['Name'] = mapData['user']['login'] 
                userName['number']['Issue'] = mapData['title']
        print(userName)

github_pull_issue()
#    return userName