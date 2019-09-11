from django.test import TestCase, Client

# Create your tests here.
class AverageTemperatureTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_invalid_sources_raises_bad_request(self):
        resp = self.c.get(
            '/api/average-temperature/123/123/',
            {'sources': 'thissourcedoesnotexist'}
        )
        self.assertEqual(resp.status_code, 400)

    def test_empty_sources_raises_bad_request(self):
        resp = self.c.get(
            '/api/average-temperature/123/123/',
            {'sources': ''}
        )
        self.assertEqual(resp.status_code, 400)

    def test_invalid_coordinates_raises_bad_request(self):
        resp = self.c.get(
            '/api/average-temperature/91/181/',
            {'sources': 'noaa'}
        )
        self.assertEqual(resp.status_code, 400)
