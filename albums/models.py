from django.db import models


class Label(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Artist(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.CharField(max_length=1000, null=True)
    year = models.IntegerField(null=True)
    catalog_number = models.CharField(max_length=255, null=True)
    labels = models.ManyToManyField(Label, null=True)
    artists = models.ManyToManyField(Artist)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
