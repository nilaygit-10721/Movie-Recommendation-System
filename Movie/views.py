from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
import textwrap
from .utils import make_suggestion

def main_view(request):
    """This View is responsible for rendering the main page.
       also it is responsible for sending back JSON response
       accroding to the conditions 

    Args:
        request : request object
    """
    if 'SearchedTitle' in request.GET:
        # get and return Serched Movie
        searched_movie = Movie.objects.get(title=request.GET.get('SearchedTitle'))
        return JsonResponse({'title':searched_movie.title,'overview':searched_movie.overview,
                             'genre':searched_movie.genre,'image':searched_movie.movie_img_url,
                             'vote_avg':searched_movie.vote_avg,'release_date':searched_movie.release_date.strftime("%Y")})
        
    if 'term' in request.GET:
        # return movie titles
        qs = Movie.objects.filter(title__istartswith=request.GET.get('term'))
        titles = list()
        for title in qs:
            titles.append(title.title)
        return JsonResponse(titles, safe=False)
    

    movies = Movie.objects.order_by('?')[:6]
    return render(request, 'Movie/main.html', context={'movies':movies})


def select_movie_ajax(request):
    """ This ajax function is responsible for stroing the user selected movies 
        and updateding the page accordingly (showing suggestions or next selection stage)

    Args:
        request : request object
    
    Returns:
        Json response : it will return a json response which contains suggested movies ( or more movies to select)
    """
    movie_id = request.GET.get('id')
    counter = request.GET.get('counter') # it can contain 1,2,3 or shuffle 
    if movie_id == "shuffle":
        # return new movies
        movies = [{'id':movie.id,'title':movie.title,'overview':textwrap.shorten(movie.overview, width=150, placeholder="..."),'movie_img_url':str(movie.movie_img_url),'genre':movie.genre,'release_date':movie.release_date.strftime("%Y")} for movie in Movie.objects.order_by('?')[:6]]
        return JsonResponse({'continue':True,'movies':movies})
    request.session[f'movie_{counter}'] = movie_id
    if int(counter) >= 3:
        # if we have selected 3 movies already , then make sugestions
        movies = make_suggestion(request.session['movie_1'],request.session['movie_2'],request.session['movie_3']) 
        return JsonResponse({'continue':False,'movies':movies})
    movies = [{'id':movie.id,'title':movie.title,'overview':textwrap.shorten(movie.overview, width=150, placeholder="..."),'movie_img_url':str(movie.movie_img_url),'genre':movie.genre,'release_date':movie.release_date.strftime("%Y")} for movie in Movie.objects.order_by('?')[:6]]
    return JsonResponse({'continue':True,'movies':movies})



