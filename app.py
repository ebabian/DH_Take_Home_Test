import requests
import json

url = "https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/ingredients.json"
headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
        }

response = requests.get(url, headers=headers)

data = response.json()

print(data)

