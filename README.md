# RESTful API for Movies WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.8
- Django (2.2)
- Django REST Framework
- Django Rest Auth

## Installation
```
	pip install django
	pip install djangorestframework
	pip install django-rest-auth
	pip install django-allauth
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have three resource, `movies`, `genre`, `poster`  so we will use the following URLS -
base url = `http://localhost:8000/api/`
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`movies` | GET | READ | Get all movies
`movies/:id` | GET | READ | Get a single movie
`movies`| POST | CREATE | Create a new movie
`movies/:id` | PUT | UPDATE | Update a movie
`movies/:id` | DELETE | DELETE | Delete a movie
`genre` | GET | READ | Get all genre
`genre/:id` | GET | READ | Get a single genre
`genre`| POST | CREATE | Create a new genre
`genre/:id` | PUT | UPDATE | Update a genre
`genre/:id` | DELETE | DELETE | Delete a genre
`poster` | GET | READ | Get all poster
`poster/:id` | GET | READ | Get a single poster
`poster`| POST | CREATE | Create a new poster
`poster/:id` | PUT | UPDATE | Update a poster
`poster/:id` | DELETE | DELETE | Delete a poster

## Use
We can test the API using django rest swagger or postman. 

You can install httpie using pip:
```
pip install django-rest-swagger
```

First, we have to start up Django's development server.
```
	python manage.py runserver
```
For admin user try this for add,delete & update:
```
	http  http://127.0.0.1:8000/admin/
```
```
username = admin
password = admin123

```

to get all movies for user try this:
```
http://localhost:8000/api/movies/
```
we get:
```
[
    {
        "popularity": 83.0,
        "director": "Victor Fleming",
        "genre": [
            {
                "name": "Adventure"
            },
            {
                "name": "Family"
            },
            {
                "name": "Fantasy"
            },
            {
                "name": "Musical"
            }
        ],
        "imdb_score": 8.3,
        "name": "The Wizard of Oz",
        "poster_id": {
            "id": 1,
            "poster_url": "http://localhost:8000/media/poster/Victor.jpg"
        }
    }
]

```

For get poster details try this:
 ```
http://localhost:8000/api/poster/
```
we get from api:
```
[
    {
        "id": 1,
        "poster_url": "http://localhost:8000/media/poster/Victor.jpg"
    }
]

```
The API has some restrictions:
-   The admin can add, remove and edit movies.
-   Only authenticated users may create, delete or edit movies.
-   Unauthenticated requests shouldn't have access.
-   User can only view the movies.



Finally, I provide a Sqlite3 and MySql DB to make these tests.

