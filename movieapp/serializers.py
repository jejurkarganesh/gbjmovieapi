from rest_framework.serializers import ModelSerializer
from . models import *




class GenreSer(ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name',]

class PosterSer(ModelSerializer):

    class Meta:
        model = Poster
        fields = ['id','poster_url',]

class MovieSer(ModelSerializer):
    genre = GenreSer(many = True)
    poster_id = PosterSer()
    class Meta:
        model = Movie
        fields = ['popularity','director','genre','imdb_score','name','poster_id',]