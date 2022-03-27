"""pile_of_shame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from viewer.models import Genre, Game
from viewer.views import GenreListView, GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView

admin.site.register(Genre)
admin.site.register(Game)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/', GenreListView.as_view(), name="genre"),
    path('game/', GameListView.as_view(), name="game"),
    path('game/new', GameCreateView.as_view(), name="create_game"),
    path('game/<int:pk>', GameDetailView.as_view(), name='game_details'),
    path('game/<int:pk>/update', GameUpdateView.as_view(), name='update_game'),
    path('game/<int:pk>/delete', GameDeleteView.as_view(), name='delete_game'),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),

]
