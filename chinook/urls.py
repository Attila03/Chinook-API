from django.conf.urls import url
from .views import (TrackDetailView, TrackListView, AlbumDetailView, AlbumListView,
                    ArtistListView, ArtistDetailView, GenreListView, GenreDetailView,
                    MediaTypeListView, MediaTypeDetailView, PlaylistDetailView, PlaylistListView)


urlpatterns = [
    url(r'^genres/$', GenreListView.as_view(), name='genre_list'),
    url(r'^genres/(?P<pk>[\w-]+)', GenreDetailView.as_view(), name='genre_detail'),
    url(r'^mediatype/$', MediaTypeListView.as_view(), name='mediatype_list'),
    url(r'^mediatype/(?P<pk>[\w-]+)', MediaTypeDetailView.as_view(), name='mediatype_detail'),
    url(r'^tracks/$', TrackListView.as_view(), name='track_list'),
    url(r'^tracks/(?P<pk>[\w-]+)', TrackDetailView.as_view(), name='track_detail'),
    url(r'^albums/$', AlbumListView.as_view(), name='album_list'),
    url(r'^albums/(?P<pk>[\w-]+)', AlbumDetailView.as_view(), name='album_detail'),
    url(r'^artists/$', ArtistListView.as_view(), name='artist_list'),
    url(r'^artists/(?P<pk>[\w-]+)', ArtistDetailView.as_view(), name='artist_detail'),
    url(r'^playlists/$', PlaylistListView.as_view(), name='playlist_list'),
    url(r'^playlists/(?P<pk>[\w-]+)', PlaylistDetailView.as_view(), name='playlist_detail'),

]