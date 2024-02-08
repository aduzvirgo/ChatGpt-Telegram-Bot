import requests

def gpt(text):
    url = "http://62.72.6.182:6699/gpt?ask=Hi"
    params = {"ask": text}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        print("HTTP Status Code:", response.status_code)  # Print the status code
        data = response.json()
        return data['answer']
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
