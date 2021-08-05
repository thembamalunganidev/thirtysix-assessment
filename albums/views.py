from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from albums.models import Album


class AlbumListView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'album_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()[:5]
        return context


class AlbumDetailView(LoginRequiredMixin, DetailView):
    template_name = 'album_detail.html'
    model = Album
