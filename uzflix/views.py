from django.views.generic import ListView, UpdateView, DeleteView, FormView, CreateView
from .models import Film, Izoh
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin


from .forms import CommentForm  # new
from django.views import View  # new
class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"


# class FilmDetailView(DetailView):
#     model = Film
#     template_name = "film_detail.html"
    

    
class FilmUpdateView(UpdateView):
    model = Film
    fields = (
        "nomi",
        "haqida",
    )
    template_name = "film_update.html"


class FilmDeleteView(DeleteView):
    model = Film
    template_name = "film_delete.html"
    success_url = reverse_lazy("film_list")





class CommentGet(DetailView):  # new
    model = Izoh
    template_name = "film_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):  # new
    model = Izoh
    form_class = CommentForm
    template_name = "film_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        matn = form.save(commit=False)
        matn = self.object
        matn.save()
        return super().form_valid(form)

    def get_success_url(self):
        film = self.get_object()
        return reverse("film_detail", kwargs={"pk": film.pk})

# class FilmDetailView(View):  # new
#     def get(self, request, *args, **kwargs):
#         view = CommentGet.as_view()
#         return view(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         view = CommentPost.as_view()
#         return view(request, *args, **kwargs)


from django.shortcuts import render, get_object_or_404

def film_detail(request, pk):
    template_name = 'film_detail.html'
    film = get_object_or_404(Film, pk=pk)
    comments = film
    new_comment = None    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.film = film
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'film': film,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


from django.shortcuts import render, redirect
from .models import Baho
from .forms import BahoForm

def rate_film(request, pk):
    film = Film.objects.get(pk=pk)

    if request.method == 'POST':
        form = BahoForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.film = film
            rating.save()
            return redirect('film_detail', pk=film.pk)  # Redirect to the film detail page
    else:
        form = BahoForm()

    return render(request, 'film_detail.html', {'form': form, 'film': film})
