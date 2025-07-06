import requests
import json

userName = {}

def github_pull_issue():
    response = requests.get(f"https://api.github.com/repos/Harshal-HP/python-github/issues")

    if response.status_code == 200:
        response_data = response.json()
        for data in response_data.items():
            userName['Name'] = data['user']['login'] 
            userName['Issue'] = data['title']
    return userName