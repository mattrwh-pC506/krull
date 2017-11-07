#Krull
=======================

This is a lightweight microframework for defining restful APIs in human readable docstrings.

## Where it is currently
Currently krull is in alpha stages, and is constantly in flux. For now, it can be reliably used to route requests to views, either class based or function based, by defining configs within docstrings.

## Where is it going
The core of krull is the definition of API schemas via docstrings. With that simple goal comes a very declaritve means for mapping API schemas to business logic. With that said, the roadmap is such:

- Database and SQLAlchemy hookup
- Declarative model 2 view serialization
- Declaritive error handling
- Declaritive validation
- Declaritive documenation generation

The plan is to base the schema on Swagger specs so that we can generate a browsable API/ documentation that correctly  maps and actually enforces parsing, validation, and serialization. 


# Examples

# Function based views

```python
from core import get_app
from responses import JsonResponse

app = get_app()

movies = [
    {"id": 1, "title": "Die Hard"},
    {"id": 2, "title": "Jurassic Park"},
    {"id": 3, "title": "Terminator"},
]

@app.endpoint
def get_movie(req):
    '''
    path: /movies/<int:movie_id>
    method: GET
    name: getmovie
    '''
    movie_id = req.path_params["movie_id"]
    movie = [m for m in movies if m["id"] == movie_id][0]
    res = JsonResponse({"data": movie}, status=200)
    return res


@app.endpoint
def post_movie(req):
    '''
    path: /movies
    method: POST
    name: postmovies
    '''
    movie = req.json
    if "title" in movie and "id" in movie:
        movies.append(movie)
        res = JsonResponse({"message": "success!"}, status=200)
    else:
        res = JsonResponse({"message": "fail!"}, status=400)
    return res
```

# Class based views
Responses are handled via a `response` method.

```python

@app.endpoint
class GetMovie:
    '''
    path: /movies/<int:movie_id>
    method: GET
    name: getmovie
    '''

    def response(self, req):
        movie_id = req.path_params["movie_id"]
        movie = [m for m in movies if m["id"] == movie_id][0]
        res = JsonResponse({"data": movie}, status=200)
        return res


@app.endpoint
class PostMovie:
    '''
    path: /movies
    method: POST
    name: postmovies
    '''
    
    def response(self, req):
        movie = req.json
        if "title" in movie and "id" in movie:
            movies.append(movie)
            res = JsonResponse({"message": "success!"}, status=200)
        else:
            res = JsonResponse({"message": "fail!"}, status=400)
        return res
```
