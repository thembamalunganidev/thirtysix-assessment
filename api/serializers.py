from rest_framework import serializers

from albums.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    labels = serializers.SerializerMethodField()
    artists = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    def get_labels(self, obj):
        return ", ".join([label.title for label in obj.labels.all()])

    def get_artists(self, obj):
        return ", ".join([artist.title for artist in obj.artists.all()])

    def get_genres(self, obj):
        return ", ".join([genre.title for genre in obj.genres.all()])

    class Meta:
        model = Album
        fields = [
            'id',
            'title',
            'cover_image',
            'year',
            'catalog_number',
            'labels',
            'artists',
            'genres',
        ]
