import json
import cgi


route_registry = {}

def route_handler(path: str, method: str, **kwargs):
    global route_registry

    def wrapper(handler):
        route_registry[path] = handler

        def registered_handler(*args, **kwargs):
            handler(*args, **kwargs)

        return registered_handler

    return wrapper


class Request:

    def __init__(self, inputdata=None):
        self.inputdata = inputdata


class Response:
    status = 200
    data = {}


class RequestHandler(BaseHTTPRequestHandler):

    def route(self):
        global route_registry
        self.handler = route_registry[self.path]
        if self.command == 'POST':

            if self.headers.get('content-type') == 'application/json':
                length = int(self.headers.get('content-length'))
                print ("LEN", length)
                parseddata = cgi.parse_qs(
                        self.rfile.read(length), 
                        keep_blank_values=1)
                self.inputdata = json.loads(
                        [k for k in parseddata][0].decode('UTF-8'))
                print ("INPUTS", self.inputdata)
            else:
                self.inputdata = {}

    def process(self, data=None):
        response = self.handler(self.request, Response())

        self.send_response(
            response.status, 
            message=self.responses[response.status][0])

        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = json.dumps(response.data)
        self.wfile.write(response.encode())

    def do_GET(self):
        self.route()
        self.request = Request()
        self.process()

    def do_POST(self):
        self.route()
        self.request = Request(inputdata=self.inputdata)
        self.process()

