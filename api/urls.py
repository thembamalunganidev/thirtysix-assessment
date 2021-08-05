from django.urls import path

from .views import AlbumListView
from .views import AlbumDetailView


urlpatterns = [
    path('', AlbumListView.as_view(), name='album-list'),
    path('<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
]
