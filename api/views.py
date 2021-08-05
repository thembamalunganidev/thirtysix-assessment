from django.db.models import Q
from django.http import Http404
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from albums.models import Album
from api.serializers import AlbumSerializer


class DatatableAwarePaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_query_param = 'draw'


class AlbumListView(generics.ListAPIView):
    serializer_class = AlbumSerializer
    pagination_class = DatatableAwarePaginator
    queryset = Album.objects.all()

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search[value]')
        filter_params = None
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(title__icontains=key.strip())
                    else:
                        filter_params |= Q(title__icontains=key.strip())
        albums = Album.objects.filter(filter_params).order_by('-year') if filter_params \
            else Album.objects.order_by('-year').all()
        serializer = AlbumSerializer(albums, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class AlbumDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            album = Album.objects.get(id=pk)
            serializer = AlbumSerializer(album)
            return Response(serializer.data)
        except Album.DoesNotExist:
            raise Http404
