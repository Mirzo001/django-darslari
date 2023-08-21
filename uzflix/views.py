from django.views.generic import ListView
from .models import Film

class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"