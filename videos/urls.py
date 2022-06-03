from django.urls import path

from . import views

urlpatterns = [
    path('/videos', views.VideosListView.as_view(), name="videos"),

]