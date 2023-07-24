#!/usr/bin/python3

import requests

response = requests.get("https://randomuser.me/api")
print(response.status_code)
data = response.json()

title = data['results'][0]['name']['title']

print(title)
