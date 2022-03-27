from django.urls import path
from viewer.views import GenreListView, GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView

app_name = 'viewer'
urlpatterns = [
    path('', GameListView.as_view(), name='game'),
    path('new/', GameCreateView.as_view(), name="create_game"),
    path('<int:pk>/', GameDetailView.as_view(), name='game_details'),
    path('<int:pk>/update', GameUpdateView.as_view(), name='update_game'),
    path('<int:pk>/delete', GameDeleteView.as_view(), name='delete_game'),
    path('genre/', GenreListView.as_view(), name="genre"),
]