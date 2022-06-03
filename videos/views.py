from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Create your views here.

class VideosListView(LoginRequiredMixin, ListView):
    model = ''
    context_object_name = 'videos_home'
    template_name: str = 'videos/videos_home.html'  # Can include it or not if the standard naming is followed
    login_url = "/admin"

    # def get_queryset(self):
    #     return self.request.user.objects.all()