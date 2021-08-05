import requests

from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

from thirtysix_assessment.config import Config


class APIRequestError(Exception):
    pass


class Discogs:
    @staticmethod
    def search(params: dict = {}, headers: dict = {}):
        try:
            endpoint = Discogs._add_params(f'{Config.DISCOGS_API_BASE}/database/search', params)
            headers = {**headers, **Discogs._authorization_header()}
            response = requests.get(endpoint, headers=headers)
            return response.json()
        except requests.exceptions.HTTPError as error:
            raise APIRequestError(error)

    @staticmethod
    def get_release_details(release_id: int, params: dict = {}, headers: dict = {}):
        try:
            endpoint = Discogs._add_params(f'{Config.DISCOGS_API_BASE}/database/search', params)
            headers = {**headers, **Discogs._authorization_header()}
            response = requests.get(endpoint, headers=headers)
            return response.json()
        except requests.exceptions.HTTPError as error:
            raise APIRequestError(error)

    @staticmethod
    def _authorization_header():
        return {'Authorization': f'Discogs key={Config.DISCOGS_API_KEY}, '
                                 f'secret={Config.DISCOGS_API_SECRET}'}

    @staticmethod
    def _add_params(url: str, params: dict):
        url_parse = urlparse(url)
        query = url_parse.query
        url_dict = dict(parse_qsl(query))
        url_dict.update(params)
        url_new_query = urlencode(url_dict)
        url_parse = url_parse._replace(query=url_new_query)
        return urlunparse(url_parse)
