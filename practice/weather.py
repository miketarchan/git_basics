#!/usr/bin/env python3
from classes import City, Weather
from datetime import datetime

USAGE = 'USAGE: {prog} CITY or LAT LON\nGet current temperature.'

def main(args):
    prog, *args = args
    if (len(args) == 1 or len(args) == 2) == False:
        exit(USAGE.format(prog=prog))

    params = {
        "name":args[0],
        "latitude": args[0] if len(args) == 2 else None,
        "longitude": args[1] if len(args) == 2 else None
    }
    weather = Weather(City(**params))
    weather_data = weather.get()
    date_obj = datetime.fromisoformat(weather_data['time'])
    
    print(f"Currently in {weather_data['city']} on {date_obj.strftime('%b %d at %A')} is {weather_data['temperature']}\u00b0C")

if __name__ == '__main__':
    import sys
    main(sys.argv)