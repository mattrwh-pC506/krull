Krull
=======================

This is a lightweight microframework for building restful APIs
::
    from krull.handlers import route_handler
    from krull.server import run_server


    @endpoint(path='/users/<int:id>', method='GET')
    def getusers(req, res, *args, **kwargs):
        res.status = 200
        user_id = kwargs.get("id")
        res.data = {"message": "Hello world, number {}!".format(user_id)}
        return res


    @endpoint(path='/users/<str:username>', method='GET')
    def getuserbyusername(req, res, *args, **kwargs):
        res.status = 200
        username = kwargs.get("username")
        res.data = {"message": "Hello world, and hey {}!".format(username)}
        return res


    @endpoint(path='/users', method='POST')
    def postusers(req, res):
        # do something with data
        res.status = 201
        res.data = {"message": "success!"}
        return res


    if __name__ == '__main__':
        run_server()
