from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . serializers import *
from . models import *
from rest_framework.permissions import AllowAny


class GenreOps(ModelViewSet):

    queryset = Genre.objects.all()
    serializer_class = GenreSer


class PosterOps(ModelViewSet):

    queryset = Poster.objects.all()
    serializer_class = PosterSer
    def get_permissions(self):
        if self.action == "list" :
            self.permission_classes = (AllowAny,)
        return super().get_permissions()

class MovieOps(ModelViewSet):
    """
            retrive:
              return a movie instance.

            list:
                Return all movies, ordered by mostly joined.

            create:
                Create a new movie

            delete:
                Delete an existing movie.

            partial_update:
                Update one or more fields on an existing movie.

            update:
                Update a movie.
        """

    queryset = Movie.objects.all()
    serializer_class = MovieSer

    def get_permissions(self):
        if self.action == "list" :
            self.permission_classes = (AllowAny,)
        return super().get_permissions()