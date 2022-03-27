from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from viewer.models import Genre, Game
from viewer.forms import GameForm


class GenreListView(ListView):
    template_name = "genre_list.html"
    model = Genre


class GameListView(ListView):
    template_name = "game_list.html"
    model = Game


class GameDetailView(DetailView):
    template_name = "game_detail_view.html"
    model = Game


class GameCreateView(CreateView):
    template_name = "forms/form.html"
    form_class = GameForm
    success_url = reverse_lazy("game")


class GameUpdateView(UpdateView):
    template_name = "forms/form.html"
    form_class = GameForm
    model = Game
    success_url = reverse_lazy("game")
