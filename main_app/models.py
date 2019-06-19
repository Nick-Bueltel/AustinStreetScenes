from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Scene(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('detail', kwargs={'scene_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for scene_id: {self.scene_id} @{self.url}"
    
    