from django.db import models

# Create your models here.
class abc(models.models):
    movie_name = models.CharField(max_length=20)
    movie_rating = models.IntegerField()
    movie_release = models.DateField()
    movie_duration = models.DurationField()
    movie_desc = models.TextField()