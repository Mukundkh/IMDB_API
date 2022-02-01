from django.urls import path
from watchlist_app.api import views
urlpatterns = [
    #function based views
    # path('list/', views.movie_list, name='movie-list'),
    # path('<int:pk>', views.movie_detail, name='movie-detail'),

    path('list/',views.MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', views.MovieDetailAV.as_view(), name='movie-detail'),
]