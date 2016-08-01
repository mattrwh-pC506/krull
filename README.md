#Krull
=======================

This is a lightweight microframework for building restful APIs

''' #python
import pytest
from core import endpoints, JsonResponse
from server import run_krull


@endpoints({
    'path': '/users/<int:id>', 
    'method': 'GET', 
    'name': "getusers",
})
def getusers(req):
    user_id = req.path_params["id"]
    message = "Hello world, number {}!".format(user_id)
    res = JsonResponse({"message": message}, status=200)
    return res


@endpoints({
    'path': '/users/<username>', 
    'method': 'GET', 
    'name': "getuserbyusername",
})
def getuserbyusername(req):
    username = req.path_params["username"]
    message = "Hello world, and hey {}!".format(username)
    res = JsonResponse({"message": message}, status=200)
    return res


@endpoints({
    'path': '/users', 
    'method': 'POST', 
    'name': "postusers",
})
def postusers(req):
    res = JsonResponse({"message": "success!"}, status=200)
    return res


if __name__ == '__main__':
    run_krull()

```
