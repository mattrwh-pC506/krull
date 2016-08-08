import sys
import json
import yaml
import inspect
import os
import importlib.util

from werkzeug.wrappers import Request, Response
from werkzeug.utils import cached_property
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import NotFound
from werkzeug.wsgi import SharedDataMiddleware


APP = None


class JsonRequest(Request):
    max_content_length = 1024 * 1024 * 4

    @cached_property
    def json(self):
        if self.headers.get('content-type') == 'application/json':
            return json.loads(self.data.decode('utf8'))
    

class Krull(object):
    
    routes = None
    endpoint_registry = []

    def dispatch_request(self, request):
        try:
            self.routes = self.rule_map.bind_to_environ(request.environ)
            self.endpoint, values = self.routes.match()
            matches = [r["view"] for r in self.endpoint_registry if r["name"] == self.endpoint]
            if not matches:
                raise NotFound("Could not resolve url.")
            request.path_params = values
            response = matches[0](request)
            return response

        except NotFound as e:
            return e.get_response()

    def wsgi_app(self, environ, start_response):
        request = JsonRequest(environ) 
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        if not self.routes:
            self.rule_map = Map([r["rule"] for r in self.endpoint_registry])
        return self.wsgi_app(environ, start_response)

    def endpoint(self, view):

        if inspect.isclass(view):
            view_name = view.__name__
            view = view()
            view.__name__ = view_name

        docstring = inspect.getdoc(view)
        configs = yaml.load(docstring)
        path = configs.get('path', '/')
        methods = [configs.get('method', 'GET')]
        name = configs.get('name', view.__name__)
        rule = Rule(path, endpoint=name, methods=methods)
        self.endpoint_registry.append({'rule': rule, 'view': view, 'name': name,})
        
        def wrapper(*args, **kwargs):
            return view(*args, **kwargs)
        
        return wrapper


def load_files(directory, file_list, main):
    for file_name in file_list:
        file_extension = file_name[-3:]
        module_name = file_name[:-3]
        abspath = directory + "/" + file_name
        if file_extension == '.py' and abspath != main:
            spec = importlib.util.spec_from_file_location(module_name, abspath)
            mod_from_spec = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod_from_spec)


def load_app():
    main = os.path.abspath(sys.modules['__main__'].__file__)
    root = os.path.dirname(main)
    project = os.walk(root)
    for level in project:
        directory = level[0]
        file_list = level[2]
        if directory.split("/")[-1] != "__pycache__":
            load_files(directory, file_list, main)


def build_app():
    global APP
    APP = Krull()
    APP.wsgi_app = SharedDataMiddleware(APP.wsgi_app, {})
    load_app()
    return APP


def get_app():
    global APP
    return APP



