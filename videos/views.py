from django.shortcuts import render
from Netflix.settings import TMDB_API_KEY
import requests

# Create your views here.

def all_movies_tvshows(request):
  return render(request, 'all-movies/home.html')

def view_all(request):

  # get now playing movies
  now_playing_movies_request = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=" + TMDB_API_KEY)
  now_playing_movies_result = now_playing_movies_request.json()
  now_playing_movies = now_playing_movies_result['results']

  # get popular tv shows
  popular_tv_shows_request = requests.get("https://api.themoviedb.org/3/tv/popular?api_key=" + TMDB_API_KEY)
  popular_tv_shows_result = popular_tv_shows_request.json()
  popular_tv_shows = popular_tv_shows_result['results']  

  # get top rated tv shows
  top_rated_tv_request = requests.get("https://api.themoviedb.org/3/tv/top_rated?api_key=" + TMDB_API_KEY)
  top_rated_tv_result = top_rated_tv_request.json()
  top_rated_tv = top_rated_tv_result['results']
   
  # get top rated movies
  top_rated_movie_request = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=" + TMDB_API_KEY)
  top_rated_movie_result = top_rated_tv_request.json()
  top_rated_movie = top_rated_tv_result['results']

  # get upcoming movies
  upcoming_movie_request = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=" + TMDB_API_KEY)
  upcoming_movie_results = upcoming_movie_request.json()
  upcoming_movies = upcoming_movie_results['results']

  return render(request,'all-movies/home.html', {'now_playing_movies': now_playing_movies, 'top_rated_movie': top_rated_movie, 'top_rated_tv':top_rated_tv, 'upcoming_movies': upcoming_movies, 'popular_tv_shows':popular_tv_shows})


  

