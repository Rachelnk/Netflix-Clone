# from django import views
# from django.urls import path

# urlpattern = [
#     path('',views.welcome,name='welcome'),
# ]
from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
]