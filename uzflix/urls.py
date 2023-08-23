from django.urls import path
from .views import FilmListView, FilmDetailView

urlpatterns = [
    path("", FilmListView.as_view(), name="film_list"),
    path("film/<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
]
