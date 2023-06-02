import json
from urllib import parse
from urllib.request import urlopen
from urllib.error import HTTPError
from exceptions import WeatherBadRequestException

def generateURL (URL, **kwargs):
    """Generate the url with proper query parameters and returns it."""
    params = dict((k, parse.urlencode(v)) for k, v in kwargs.items())
    return URL.format(**params)

def get_json_data_from_url(url):
    """
    Implementation of simple data loading from external URL.
    """
    try:
        response = urlopen(url)
        data = response.read()
        data = data.decode('utf-8')
        return json.loads(data)
    except HTTPError :
        raise WeatherBadRequestException

if __name__ == '__main__':
    expect_url = "https://test.com?key=val&k2=v2"
    generated_url = generateURL('https://test.com?{params}',**{"params":{"key":"val","k2":"v2"}})
    assert generated_url == expect_url, "Failed url generation"

    url = 'https://geocoding-api.open-meteo.com/v1/search?name=Lviv'
    assert type(get_json_data_from_url(url=url)) == dict, "Fetch data failed, bad response"



