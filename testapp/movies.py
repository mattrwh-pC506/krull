from core import get_app
from responses import JsonResponse

app = get_app()

movies = [
        {"id": 1, "title": "Die Hard"},
        {"id": 2, "title": "Jurassic Park"},
        {"id": 3, "title": "Terminator"},
        ]

@app.endpoint
class GetMovies:
    '''
    path: /movies
    method: GET
    name: getmovies
    '''

    def response(self, req):
        res = JsonResponse({"data": movies}, status=200)
        return res


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
class GetMovieByTitle:
    '''
    path: /movies/<title>
    method: GET
    name: getmoviebytitle
    '''

    def response(self, req):
        title = req.path_params["title"]
        movie = [m for m in movies if m["title"] == title][0]
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
