from django.urls import path
from . import views

app_name='game'
urlpatterns = [
    path('',views.index,name="index"),
    path('movie_update/',views.update_movie,name="update_movie"),
    path('my_movie_list/',views.my_movie_list,name="my_movie_list"),
]
