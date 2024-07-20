import requests
import os

url = 'https://jsonplaceholder.typicode.com'
name = 'json_file'

response = requests.get(url)
response.raise_for_status
os.makedirs(name, exist_ok=True)

for i, item in enumerate():
    file_name = f"{name}/object_{i+1}.json"
    with open(file_name, 'w') as f:
      import json
      json.dump(item, f, indent=4)