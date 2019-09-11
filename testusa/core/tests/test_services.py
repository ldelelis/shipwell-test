from django.test import TestCase

from core.services import AverageTemperatureService
from core.exceptions import NonExistentServiceException

class AverageTemperatureServiceTestCase(TestCase):
    def test_invalid_source_raises_exception(self):
        data = {
            'sources': '1,2,3',
            'latitude': 1,
            'longitude': 1
        }
        service = AverageTemperatureService(**data)
        self.assertRaises(NonExistentServiceException, service.get_average_temperatures)

    def test_average_temperatures_returns_float_fahrenheit(self):
        data = {
            'sources': ['noaa', 'accuweather', 'weather.com'],
            'latitude': 1,
            'longitude': 1
        }
        service = AverageTemperatureService(**data)
        temp = service.get_average_temperatures().get('fahrenheit')
        self.assertEqual(float, type(temp))

    def test_average_temperatures_returns_int_celsius(self):
        data = {
            'sources': ['noaa', 'accuweather', 'weather.com'],
            'latitude': 1,
            'longitude': 1
        }
        service = AverageTemperatureService(**data)
        temp = service.get_average_temperatures().get('celsius')
        self.assertEqual(int, type(temp))

