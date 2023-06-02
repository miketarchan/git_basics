class WeatherException(Exception):
    pass


class WeatherBadRequestException(WeatherException):
    pass


class CityLoadCoordinatesException(WeatherException):
    
    def __init__(self, name, *args):
        super().__init__(f"Failed to load {name!r} coordinates",*args)


class WrongCityProvidedException(WeatherException):
    pass