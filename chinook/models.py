from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=160)
    artist = models.ForeignKey("Artist", related_name='albums', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}".format(self.title)


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=120)

    def __str__(self):
        return "{}".format(self.name)


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.name)


class MediaType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.name)


class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __str__(self):
        return "{}".format(self.name)


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey("Playlist")
    track = models.ForeignKey("Track")

    class Meta:
        unique_together = ('playlist', 'track')

    def __str__(self):
        return "Playlist {}: {}".format(self.playlist, self.track)


class Track(models.Model):
    id = models.AutoField(primary_key=True)
    playlist = models.ManyToManyField(Playlist, through=PlaylistTrack, related_name='tracks')
    name = models.CharField(max_length=200)
    album = models.ForeignKey("Album", null=True, blank=True, related_name='tracks')
    mediatype = models.ForeignKey("MediaType")
    genre = models.ForeignKey("Genre", null=True, blank=True)
    composer = models.CharField(max_length=220, blank=True, null=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)



