from django import views
from django.urls import path

urlpattern = [
    path('',views.welcome,name='welcome'),
]