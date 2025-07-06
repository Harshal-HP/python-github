import requests

userName = {}

response = requests.get(f"https://api.github.com/repos/Harshal-HP/python-github/issues")

if response.status_code == 200:
    response_data = response.json()
    for data in response_data:
        userName[data['user']['login']] = data['title']


