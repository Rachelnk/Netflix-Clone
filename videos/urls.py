
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('videos_home/', views.VideosListView.as_view(), name="videos_home"),

]