from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to = 'profile/')

class Movie(models.Model):
    title:models.CharField(max_length=225)
    description:models.TextField() 
    
       
class Video(models.Model):
    title:models.CharField(max_length=225)
    description:models.TextField() 