from django.urls import path, re_path
from . import views

urlpatterns = [
  path('', views.view_all, name='home'),
  path('navbar/', views.load_navbar, name = 'navbar')
]