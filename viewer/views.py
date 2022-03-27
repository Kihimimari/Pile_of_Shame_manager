from django.shortcuts import render
from django.views.generic import ListView, DetailView
from viewer.models import Genre, Game


class GenreListView(ListView):
    template_name = "genre_list.html"
    model = Genre


class GameListView(ListView):
    template_name = "game_list.html"
    model = Game


class GameDetailView(DetailView):
    template_name = "game_detail_view.html"
    model = Game
