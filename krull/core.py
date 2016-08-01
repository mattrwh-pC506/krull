import json

from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import NotFound
from werkzeug.wsgi import SharedDataMiddleware

from responses import JsonResponse


class Krull(object):
    
    routes = None

    def get_registry(self):
        return endpoints.registry

    def dispatch_request(self, request):
        try:
            self.routes = self.rule_map.bind_to_environ(request.environ)
            endpoint, values = self.routes.match()
            matches = [r["view"] for r in self.get_registry() if r["name"] == endpoint]
            if not matches:
                raise NotFound("Could not resolve url.")
            request.path_params = values
            response = matches[0](request)
            return response

        except NotFound as e:
            return e.get_response()

    def spawn(self, environ, start_response):
        request = Request(environ) 
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        if not self.routes:
            self.rule_map = Map([r["rule"] for r in self.get_registry()])
        return self.spawn(environ, start_response)
        

def spawn_krull():
    krull = Krull()
    krull.spawn = SharedDataMiddleware(krull.spawn, {})
    return krull


def endpoints(configs):
    
    if not hasattr(endpoints, 'registry'):
        endpoints.registry = []

    def wrapper(view):
        path = configs.get('path', '/')
        methods = [configs.get('method', 'GET')]
        name = configs.get('name', view.__name__)
        rule = Rule(path, endpoint=name, methods=methods)
        endpoints.registry.append({'rule': rule, 'view': view, 'name': name,})

        def registered_view(*args, **kwargs):
            return view(*args, **kwargs)

        return registered_view

    return wrapper


