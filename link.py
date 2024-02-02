import requests

url = "http://localhost"
response = requests.get(url)

print(response.text)
