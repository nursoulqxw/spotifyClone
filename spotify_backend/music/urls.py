from rest_framework.routers import DefaultRouter
from .views import SongViewSet, ArtistViewSet, AlbumViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='song')
router.register(r'artists', ArtistViewSet, basename='artist')
router.register(r'albums', AlbumViewSet, basename='album')

e='song-list
urlpatterns = [
    path('songs/', SongViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('songs/<int:pk>/', SongViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('artists/', ArtistViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('artists/<int:pk>/', ArtistViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('albums/', AlbumViewSet.as_view({'get': 'list', 'post': 'create'}), name='album-list'),
    path('albums/<int:pk>/', AlbumViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('songs/', SongViewSet.as_view()),
    # path('artists/', ArtistViewSet.as_view()),
    # path('albums/', AlbumViewSet.as_view()),
    # path('songs/<int:song_id>/', SongViewSet.as_view()),
    # path('artists/<int:artist_id>/', ArtistViewSet.as_view()),
    # path('albums/<int:album_id>/', AlbumViewSet.as_view()),
]