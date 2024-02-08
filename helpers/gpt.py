import logging

logging.basicConfig(level=logging.DEBUG)

def gpt(text):
    url = "http://62.72.6.182:6699/gpt"
    params = {"ask": text}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        logging.debug(f"API Response: {data}")
        return data['answer']
    except requests.exceptions.RequestException as e:
        logging.error(f"Error: {e}")
        return None
