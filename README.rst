Krull
=======================

This is a lightweight microframework for building restful APIs
::
    from krull.handlers import endpoint
    from krull.server import run_server


    @endpoint(path='/users/<int:id>', method='GET')
    def getusers(req, res):
        user_id = req.path_params["id"]
        res.data = {"message": "Hello world, number {}!".format(user_id)}
        res.status = 200
        return res


    @endpoint(path='/users/<str:username>', method='GET')
    def getuserbyusername(req, res):
        username = req.path_params["username"]
        res.data = {"message": "Hello world, and hey {}!".format(username)}
        res.status = 200
        return res


    @endpoint(path='/users', method='POST')
    def postusers(req, res):
        # do something with data
        res.data = {"message": "success!"}
        res.status = 201
        return res


    if __name__ == '__main__':
        run_server()
