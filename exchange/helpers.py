import requests
import json


def fetch_data(url):
    response = requests.get(url)
    data = json.loads(response.content)
    return data


if __name__ == '__main__':
    pass
