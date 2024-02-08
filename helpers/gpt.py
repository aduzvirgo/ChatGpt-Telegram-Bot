import requests

url = "http://62.72.6.182:6699/gpt?ask=Hi"
params = {
    "ask": "hello world"
}

response = requests.get(url, params=params)
data = response.json()

print(data)
