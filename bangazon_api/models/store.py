from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    favorites = models.ManyToManyField(User, related_name='favorites', through="Favorite")

    def __str__(self):
        return self.name
