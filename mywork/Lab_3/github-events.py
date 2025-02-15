#!/usr/bin/python3
import os
import json
import requests

GHUSER = os.getenv('sakedir04')
url = 'https://api.github.com/users/{GHUSER}/events'
response = requests.get(url)
events = json.loads(response.text)

for event in events[:5]:
    print(event['type'], '::', event['repo']['name'])

