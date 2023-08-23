from django.views.generic import ListView
from .models import Film
from django.views.generic import DetailView


class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"


class FilmDetailView(DetailView):
    model = Film
    template_name = "film_detail.html"

    