import requests
import json
import sys

url = 'https://emkc.org/api/v1/piston/execute'

json_file = sys.argv[1]

with open(json_file) as data:
    packet = json.load(data)

response = requests.request('POST', url, data=packet)
print(response.text)