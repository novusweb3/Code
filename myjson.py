import json
import requests

with open("response2.json", "r") as f:
        data = json.load(f)

print(data)