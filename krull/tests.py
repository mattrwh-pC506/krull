import pytest

from core import endpoint
from responses import JsonResponse
from server import run_krull


@endpoint
class GetUsers:
    '''
    path: /users
    method: GET
    name: getusers
    '''

    def __call__(self, req):
        message = "Hello all users!"
        res = JsonResponse({"message": message}, status=200)
        return res


@endpoint
def getuser(req):
    '''
    path: /users/<int:user_id>
    method: GET
    name: getuser
    '''
    user_id = req.path_params["user_id"]
    message = "Hello world, number {}!".format(user_id)
    res = JsonResponse({"message": message}, status=200)
    return res


@endpoint
def getuserbyusername(req):
    '''
    path: /users/<username>
    method: GET
    name: getuserbyusername
    '''
    username = req.path_params["username"]
    message = "Hello world, and hey {}!".format(username)
    res = JsonResponse({"message": message}, status=200)
    return res


@endpoint
def postusers(req):
    '''
    path: /users
    method: POST
    name: postusers
    '''
    res = JsonResponse({"message": "success!"}, status=200)
    return res


if __name__ == '__main__':
    run_krull()

