from django.contrib import admin

from .models import (Artist, Album, Customer, Employee, Genre,
                     Invoice, Invoiceline, MediaType, Playlist, PlaylistTrack, Track)


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Genre)
admin.site.register(Invoice)
admin.site.register(Invoiceline)
admin.site.register(MediaType)
admin.site.register(Playlist)
admin.site.register(PlaylistTrack)
admin.site.register(Track)
