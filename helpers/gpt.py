import requests

def gpt(hello world):
    url = "https://freegptapi.hop.sh/neural/api"
    params = {
    "query": "hello world"}
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
