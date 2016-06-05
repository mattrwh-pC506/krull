Krull
=======================

This is a lightweight microframework for building restful APIs
::
    from krull.handlers import route_handler
    from krull.server import run_server


    @route_handler(path='/users', method='GET')
    def getusers(req, res):
        res.status = 200
        res.data = {"message": "Hello world!"}
        return res


    @route_handler(path='/users', method='POST')
    def postusers(req, res):
        # do something with data
        res.status = 201
        res.data = {"message": "success!"}
        return res


    if __name__ == '__main__':
        run_server()
