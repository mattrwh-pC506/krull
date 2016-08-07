import pytest
from core import endpoints, JsonResponse
from server import run_krull


@endpoint
class GetUsers:
    '''
    path: /users/<int:user_id>
    method: GET
    name: getusers
    '''

    def dispatch_request(self):
        message = "Hello world, number {}!".format(self.user_id)
        res = JsonResponse({"message": message}, status=200)
        return res



@endpoint
def getuser(req):
    '''
    path: /users
    method: GET
    name: getuser
    '''
    message = "Hello list of users!"
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

