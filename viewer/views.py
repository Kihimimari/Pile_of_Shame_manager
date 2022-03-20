from django.shortcuts import render
from django.views.generic import ListView
from viewer.models import Genre


class GenreListView(ListView):
    template_name = "genres.html"
    model = Genre
