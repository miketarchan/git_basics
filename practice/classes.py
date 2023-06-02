from helpers import generateURL, get_json_data_from_url
from exceptions import *

class City:
    """
    Class that represents minimum data for proper loading
    longitude and latitute in case if they were not provided during initialization.

    This class could work in two scenarions:
        - when user provided full necessary data such as name, lat and lon.
        - when user provided just only city's name. In this case the class will try
            to automatically detect lat and lon by fetching those data from external service 
            provided in URL property.

    Attributes
    ----------
    name : str
        city's name
    latitude : float
        city's latitude
    lolongitude : float
        city's longitude

    
    Methods
    -------
    get_coord():
        returns dict with latitude and longitude keys representively.
    """

    URL = "https://geocoding-api.open-meteo.com/v1/search?{params}"

    def __init__(self, name, latitude=None, longitude=None):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_coord(self):
        """
        Return the latitude and longitude coordinates if they are valid
        Elsewhere try to load them from external source and return the result.

        Returns
        -----
        {"latitude": float|None, "longitude": float|None}

        Raises
        ------
        CityLoadCoordinatesException if it fails to load city coordinates.

        """
        empty_data = {'latitude':None, 'longitude': None}

        if isinstance(self.latitude, float) and isinstance(self.longitude, float):
            return {'latitude': self.latitude, 'longitude':self.longitude}
        
        try:
            data = get_json_data_from_url(
                generateURL(
                    City.URL,
                    **{
                        'params': {
                            "name":self.name
                        }
                    }
                )
            )
    
            results = list(data['results'] if 'results' in data else [])
            if len(results) == 0:
                return empty_data
            
            self.name = results[0]['name']

            return {'latitude':results[0]['latitude'], 'longitude': results[0]['longitude']}

        except WeatherBadRequestException:
            raise CityLoadCoordinatesException(self.name)


class Weather:
    """
    Class that represents weather object

    Attributes
    ----------
    city : City
        Object of City

    Methods
    -------
    get():
        Return the weather's data such as temperature, windspeed, time and others

    Raises
    ------
    WeatherException if any weather related exception occurs
    """
    URL = "https://api.open-meteo.com/v1/forecast?{params}"
    
    def __init__(self, city: City):
        if isinstance(city, City) == False:
            raise WrongCityProvidedException("Wrong City object provided")
        
        self.city = city

    def get(self):
        """
        Fetching the actual data
        """
        params = self.city.get_coord()
        params['current_weather'] = True
        data = get_json_data_from_url(
            generateURL(
                Weather.URL,
                **{
                    "params":params
                }
            )
        )
        
        return {
            "city": self.city.name,
            "temperature": data['current_weather']['temperature'],
            "time": data['current_weather']['time'],
        }


if __name__ == '__main__':
    weather = Weather(City(name="Kyiv"))
    print(weather.get())



