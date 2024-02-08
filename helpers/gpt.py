import requests

def gpt(text):
    url = "http://62.72.6.182:6699/gpt?ask=Hi"
    params = {"ask": text}
    response = requests.get(url, params=params)
    data = response.json()
    return data['answer']
