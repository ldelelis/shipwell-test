import requests

from testusa.settings import WEATHER_SERVICE_URL
from .exceptions import NonExistentServiceException

class TemperatureService:
    """Base class for temperature services.
    Must implement `get_request_data`, `url`, and `method`
    """
    url = None
    method = None

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def get_request_data(self):
        raise NotImplementedError()

    def make_request(self):
        if self.method == 'GET':
            ret = requests.get(
                "%s/%s%s" % (WEATHER_SERVICE_URL, self.url, self.get_request_data())
            )
        elif self.method == 'POST':
            ret = requests.post(
                "%s/%s" % (WEATHER_SERVICE_URL, self.url),
                json=self.get_request_data()
            )
        ret.raise_for_status()
        return ret.json()

class AccuweatherTemperatureService(TemperatureService):
    url = 'accuweather'
    method = 'GET'

    def get_request_data(self):
        return "?latitude=%s&longitude=%s" % (
            self.lat,
            self.lon
        )

    def get_temperature(self):
        data = self.make_request() \
                   .get('simpleforecast') \
                   .get('forecastday')[0] \
                   .get('current')
        return float(data.get('fahrenheit'))

class NoaaTemperatureService(TemperatureService):
    url = 'noaa'
    method = 'GET'

    def get_request_data(self):
        return "?latlon=%s,%s" % (
            self.lat,
            self.lon
        )

    def get_temperature(self):
        data = self.make_request() \
                   .get('today') \
                   .get('current')
        return float(data.get('fahrenheit'))

class WeatherdotcomTemperatureService(TemperatureService):
    url = 'weatherdotcom'
    method = 'POST'

    def get_request_data(self):
        return {
            'lat': self.lat,
            'lon': self.lon
        }

    def get_temperature(self):
        data = self.make_request() \
                   .get('query') \
                   .get('results') \
                   .get('channel') \
                   .get('condition')
        return float(data.get('temp'))

class AverageTemperatureService:
    """Collects services of external weather APIs to calculate an average
    temperature
    """
    def __init__(self, sources=None, latitude=None, longitude=None):
        self.sources = sources
        self.lat = latitude
        self.lon = longitude

    def to_celsius(self, temp):
        return int(round((temp - 32) * 5 / 9))

    def get_temperature_service(self, source):
        return {
            'noaa': NoaaTemperatureService,
            'accuweather': AccuweatherTemperatureService,
            'weather.com': WeatherdotcomTemperatureService
        }.get(source, None)

    def get_average_temperatures(self):
        length_services = len(self.sources)
        temperatures = []

        for source in self.sources:
            temperature_service = self.get_temperature_service(source)
            if temperature_service is None:
                raise NonExistentServiceException(source)
            temperature = temperature_service(self.lat, self.lon).get_temperature()
            temperatures.append(temperature)

        average_temperature = sum(temperatures) / length_services

        return {
            'fahrenheit': average_temperature,
            'celsius': self.to_celsius(average_temperature)
        }

