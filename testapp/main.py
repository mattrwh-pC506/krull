from core import get_app
from responses import HttpResponse

app = get_app()

@app.endpoint
class GetMain:
    '''
    path: /
    method: GET
    name: getmain
    '''

    def __call__(self, req):
        res = HttpResponse("<h1>hello <em>world</em></h1>", status=200)
        return res
