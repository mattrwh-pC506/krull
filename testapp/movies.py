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

    def __call__(self, req):
        res = JsonResponse({"data": movies}, status=200)
        return res


@app.endpoint
def getmovie(req):
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
def getmoviebytitle(req):
    '''
    path: /movies/<title>
    method: GET
    name: getmoviebytitle
    '''
    title = req.path_params["title"]
    movie = [m for m in movies if m["title"] == title][0]
    res = JsonResponse({"data": movie}, status=200)
    return res


@app.endpoint
def postmovie(req):
    '''
    path: /movies
    method: POST
    name: postmovies
    '''
    body = req.data
    print ("BODY", body)
    res = JsonResponse({"message": "success!"}, status=200)
    return res
