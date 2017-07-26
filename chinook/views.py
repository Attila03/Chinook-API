from django.db.models import Q

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import filters

from .serializers import (TrackGETSerializer,  AlbumGETSerializer,
                          AlbumPOSTSerializer, ArtistGETSerializer, ArtistListSerializer,
                          GenreSerializer, MediaTypeSerializer, PlaylistGETSerializer, PlaylistPOSTSerializer)
from .models import (Artist, Album, Customer, Employee, Genre,
                      Invoice, Invoiceline, MediaType, Playlist, PlaylistTrack, Track)
from .pagination import TrackPagination
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, SAFE_METHODS


# Genre

class GenreListView(generics.ListCreateAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]
    

# Media

class MediaTypeListView(generics.ListCreateAPIView):

    queryset = MediaType.objects.all()
    serializer_class = MediaTypeSerializer


class MediaTypeDetailView(generics.RetrieveDestroyAPIView):

    queryset = MediaType.objects.all()
    serializer_class = MediaTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class TrackListView(generics.ListAPIView):

    queryset = Track.objects.all()
    serializer_class = TrackGETSerializer
    pagination_class = TrackPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name']

    def get_queryset(self, *args, **kwargs):
        #print(self.request.GET)
        queryset_list = super(TrackListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            return queryset_list.filter(
                Q(name__icontains=query)
            )
        return queryset_list


class TrackDetailView(generics.RetrieveAPIView):

    queryset = Track.objects.all()
    serializer_class = TrackGETSerializer
    permission_classes = [IsAdminOrReadOnly]


class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumGETSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):

        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        if self.request.method in ('POST', 'PUT'):
            return AlbumPOSTSerializer
        else:
            return self.serializer_class


class AlbumListView(generics.ListCreateAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumGETSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (filters.SearchFilter, )
    search_fields = ['title', 'artist__name']

    def get_serializer_class(self):

        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        if self.request.method not in SAFE_METHODS:
            return AlbumPOSTSerializer
        else:
            return self.serializer_class


class ArtistDetailView(generics.RetrieveAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistGETSerializer
    permission_classes = [IsAdminOrReadOnly]


class ArtistListView(generics.ListAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistGETSerializer
    permission_classes = [IsAdminOrReadOnly]


class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistGETSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # def perform_update(self, serializer):
    #     pass

    def get_serializer_class(self):

        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        if self.request.method not in SAFE_METHODS:
            return PlaylistPOSTSerializer
        else:
            return self.serializer_class


class PlaylistListView(generics.ListCreateAPIView):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistGETSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):

        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        if self.request.method not in SAFE_METHODS:
            return PlaylistPOSTSerializer
        else:
            return self.serializer_class

