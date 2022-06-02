from django.shortcuts import render
from Netflix.settings import TMDB_API_KEY
import requests

# Create your views here.

def view_all(request):
  now_playing_movies_request = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=" + TMDB_API_KEY)
  now_playing_movies_result = now_playing_movies_request.json()
  now_playing_movies = now_playing_movies_result['results']

  top_rated_tv_request = requests.get("https://api.themoviedb.org/3/tv/top_rated?api_key=" + TMDB_API_KEY)
  top_rated_tv_result = top_rated_tv_request.json()
  top_rated_tv = top_rated_tv_result['results']

  return render(request,'all-movies-tvs.html', {'now_playing_movies': now_playing_movies,})

