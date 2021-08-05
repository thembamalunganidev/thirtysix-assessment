from django.urls import path

from .views import AlbumListView, AlbumDetailView

urlpatterns = [
    path('', AlbumListView.as_view(), name='album-listing'),
    path('<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
]
