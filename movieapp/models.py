from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Poster(models.Model):
    poster_url = models.ImageField(upload_to='poster/', max_length=255)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    popularity = models.FloatField()
    imdb_score = models.FloatField()
    genre = models.ManyToManyField(Genre, related_name='movies')
    poster_id = models.ForeignKey(Poster, on_delete=models.CASCADE)