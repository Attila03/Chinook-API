from rest_framework import serializers
from .models import (Artist, Album, Customer, Employee, Genre,
                     MediaType, Playlist, PlaylistTrack, Track)


# GENRE


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


# MEDIA

class MediaTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaType
        fields = '__all__'


# ARTIST

class AlbumForArtistSerializer(serializers.RelatedField):

    def to_representation(self, value):
        return "{}: {}".format(value.id, value.title)


class ArtistGETSerializer(serializers.ModelSerializer):

    albums = AlbumForArtistSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'albums']


class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ['id', 'name', ]


# ALBUMS

class AlbumGETSerializer(serializers.ModelSerializer):

    artist = ArtistListSerializer()
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'tracks', 'artist']


class AlbumPOSTSerializer(serializers.ModelSerializer):

    # artist = serializers.SerializerMethodField()
    #
    # def get_artist(self, object):
    #     return object.artist.name

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'tracks']


# TRACKS

class PlaylistForTrackSerializer(serializers.RelatedField):

    def to_representation(self, value):
        return "{}: {}".format(value.id, value.name)


class AlbumForTrackDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ['id', 'title']


class TrackGETSerializer(serializers.ModelSerializer):

    album = AlbumForTrackDetailSerializer()
    playlist = PlaylistForTrackSerializer(many=True, read_only=True)

    # album = serializers.SerializerMethodField()
    #
    # def get_album(self, obj):
    #     return AlbumForTrackDetailSerializer(obj.album).data

    class Meta:
        model = Track
        fields = '__all__'


# PLAYLIST

# class PlaylistTracksSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = PlaylistTrack
#         fields = '__all__'

class TrackForPlaylistSerializer(serializers.RelatedField):

    queryset = Track.objects.all()

    def to_representation(self, value):
        return "{}: {}".format(value.id, value.name)


class PlaylistGETSerializer(serializers.ModelSerializer):

    tracks = TrackForPlaylistSerializer(many=True, read_only=False)

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'tracks']


class PlaylistPOSTSerializer(serializers.ModelSerializer):

    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Track.objects.all(), required=False)

    def create(self, validated_data):
        track_list = []
        if validated_data.get('tracks'):
            track_list = validated_data.pop('tracks')
        playlist = Playlist.objects.create(**validated_data)
        for track in track_list:
            PlaylistTrack.objects.create(playlist=playlist, track=track)
        return playlist

    def update(self, instance, validated_data):
        # print(validated_data)
        track_list = []
        # user = validated_data.pop('user')
        if validated_data.get('tracks'):
            track_list = validated_data.pop('tracks')
        PlaylistTrack.objects.filter(playlist=instance).delete()
        for track in track_list:
            PlaylistTrack.objects.create(playlist=instance, track=track)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'tracks']




