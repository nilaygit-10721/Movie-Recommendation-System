from collections import Counter 
from .models import Movie
import textwrap

def check_common_genre(genre_one,genre_two,genre_three):
    """This function is responsible for finding users favourite genres based on his/her selections

    Args:
        genre_one (str): genre of first selected movie
        genre_two (str): genre of second selected movie
        genre_three (str): genre of third selected movie

    Returns:
        list : it will return a list which contains 3 most common genre 
    """
    genres = f"{genre_one}, {genre_two}, {genre_three}"
    chosen_genres = genres.split(', ')
    genre_counter = Counter(chosen_genres)
    fav_genres= [common[0] for common in genre_counter.most_common(3)]
    fav_genres.append(', '.join(fav_genres[:3]))
    return fav_genres


def make_suggestion(first_movie_genre,second_movie_genre,third_movie_genre):
    """_summary_

    Args:
        first_movie_genre (str): genre of first selected movie
        second_movie_genre (str): genre of first selected movie
        third_movie_genre (str): genre of first selected movie

    Returns:
        list : it will return a list of dictionaries which contain suggested movies
            
                # example --> [
                               {'id': 9121, 'title': 'Mishima: A Life in Four Chapters', 'overview': 'A fictional... ', 'movie_img_url': 'img_url', 'genre': 'Drama', 'release_date': '1985'},
                               {'id': 8947, 'title': 'Joshua Tree', 'overview': 'Wellman Santee...', 'movie_img_url': 'img_url', 'genre': 'Action', 'release_date': '1993}
                              ]
    """
    first_movie_genre = Movie.objects.get(id=first_movie_genre ).genre
    second_movie_genre = Movie.objects.get(id=second_movie_genre).genre
    third_movie_genre = Movie.objects.get(id=third_movie_genre).genre
    common_genre=check_common_genre(first_movie_genre,second_movie_genre,third_movie_genre)
    if len(common_genre) != 0:
        combine_geners = Movie.objects.filter(genre=common_genre[-1]).distinct().order_by('?')[:24]
        suggested_movies = combine_geners | Movie.objects.filter(genre__in=common_genre[:-1]).distinct().order_by('?')[:24]
    else:
        suggested_movies = Movie.objects.filter(genre__in=[first_movie_genre,second_movie_genre,third_movie_genre]).distinct().order_by('?')[:24]
    
    movies = [{'id':movie.id,'title':movie.title,'overview':textwrap.shorten(movie.overview, width=150, placeholder="..."),'movie_img_url':str(movie.movie_img_url),'genre':movie.genre,'release_date':movie.release_date.strftime("%Y")} for movie in suggested_movies]
    return movies

