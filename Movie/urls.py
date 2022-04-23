from django.urls import path
from . import views
urlpatterns = [
    path('',views.main_view, name="main-page"),
    path('select_movie/',views.select_movie_ajax, name="select_movie")
]
