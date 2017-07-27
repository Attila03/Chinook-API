from django.contrib import admin

from .models import (Artist, Album, Genre,
                     MediaType, Playlist, PlaylistTrack, Track)


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(MediaType)
admin.site.register(Playlist)
admin.site.register(PlaylistTrack)
admin.site.register(Track)
