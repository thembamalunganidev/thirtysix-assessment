from django.contrib import admin

from albums.models import Album, Artist, Label, Genre

admin.site.register(Artist)
admin.site.register(Label)
admin.site.register(Album)
admin.site.register(Genre)
