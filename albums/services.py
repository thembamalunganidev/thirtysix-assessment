from django.db import models

from albums.integrations import Discogs
from albums.models import Artist, Label, Album, Genre


class DiscogsSyncService:
    @classmethod
    def perform_sync(cls, params: dict = {}):
        response = Discogs.search(params)
        cls.process_response(response)

    @classmethod
    def process_response(cls, response):
        results = response['results']
        for result in results:
            cls.process_result(result)

    @classmethod
    def process_result(cls, result):
        album = cls._find(Album, {'catalog_number': result['catno']})
        album.cover_image = result['cover_image']
        album.title = result['title']
        album.year = result['year']
        album.catalog_number = result['catno']
        album.save()

        for label_name in result['label']:
            label = cls._find(Label, {'title': label_name})
            album.labels.add(label)

        for genre_name in result['genre']:
            genre = cls._find(Genre, {'title': genre_name})
            album.genres.add(genre)

        artist = cls._find(Artist, {'title': '36'})
        album.artists.add(artist)

    @classmethod
    def _find(cls, model: models.Model, condition):
        obj = None
        try:
            obj = model.objects.get(**condition)
            obj.save()
        except model.DoesNotExist:
            pass

        if not obj:
            obj = model.objects.create(**condition)
            obj.save()
        return obj


