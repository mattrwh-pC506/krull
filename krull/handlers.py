from http.server import BaseHTTPRequestHandler
import json
import cgi
import re


route_registry = []

def build_route_pattern(route):
    route = re.sub(r'(<int:\w+>)', r'(?P\1\d+)', route)
    route = re.sub(r'(<str:\w+>)', r'(?P\1\w+)', route)

    has_int = re.search("int:", route)
    if has_int:
        route = route[:has_int.start()] + route[has_int.end():]

    has_str = re.search("str:", route)
    if has_str:
        route = route[:has_str.start()] + route[has_str.end():]
    return re.compile("^{}$".format(route))


def endpoint(path: str, method: str, **kwargs):
    global route_registry

    def wrapper(handler):
        route_registry.append((build_route_pattern(path), handler))

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

        self.route_and_handler = [
                path for path in route_registry 
                    if path[0].match(self.path)
                ][0]
        if self.route_and_handler:
            self.handler = self.route_and_handler[1]
            self.path_params = self.route_and_handler[0].match(self.path).groupdict()

        if self.command == 'POST':

            if self.headers.get('content-type') == 'application/json':
                length = int(self.headers.get('content-length'))
                parseddata = cgi.parse_qs(
                        self.rfile.read(length), 
                        keep_blank_values=1)
                self.inputdata = json.loads(
                        [k for k in parseddata][0].decode('UTF-8'))
            else:
                self.inputdata = {}

    def process(self, data=None):
        self.request.path_params = self.path_params
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

