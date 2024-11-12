# Movie/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name="main-page"),
    path('select_movie/', views.select_movie_ajax, name="select_movie"),
    path('movies/', views.movie_list, name='movie_list'),                    # List view
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),       # Detail view
    path('movies/new/', views.movie_create, name='movie_create'),            # Create view
    path('movies/<int:pk>/edit/', views.movie_update, name='movie_update'),  # Update view
    path('movies/<int:pk>/delete/', views.movie_delete, name='movie_delete') # Delete view
]
