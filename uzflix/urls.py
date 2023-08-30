from django.urls import path
from .views import FilmListView, FilmUpdateView, FilmDeleteView, film_detail, rate_film

urlpatterns = [
    path("", FilmListView.as_view(), name="film_list"),
    # path("film/<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path('film/<int:pk>/', film_detail, name='film_detail'),
    path('film/<int:pk>/rate/', rate_film, name='rate_film'),
    path("film/<int:pk>/edit/", FilmUpdateView.as_view(), name="film_update"),
    path("film/<int:pk>/delete/", FilmDeleteView.as_view(), name="film_delete"),
]
