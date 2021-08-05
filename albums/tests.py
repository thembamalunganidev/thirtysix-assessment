from django.test import TestCase

from albums.integrations import Discogs


class TestDiscogsIntegration(TestCase):
    def test_can_get_data(self):
        params = {
            'artist': '36'
        }
        response = Discogs.search(params)
        assert 'results' in response
