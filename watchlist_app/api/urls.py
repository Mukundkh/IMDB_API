from django.urls import path
from watchlist_app.api import views
urlpatterns = [
    #function based views
    # path('list/', views.movie_list, name='movie-list'),
    # path('<int:pk>', views.movie_detail, name='movie-detail'),

    path('list/',views.WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', views.WatchDetailAV.as_view(), name='watch-detail'),
]
