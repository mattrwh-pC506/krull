import json

from werkzeug.wrappers import Response


class JsonResponse(Response):
    
    def __init__(self, data, *args, **kwargs):
        json_data = json.dumps(data)
        return super().__init__(json_data, *args, **kwargs)


class HttpResponse(Response):
    
    def __init__(self, data, *args, **kwargs):
        kwargs["mimetype"] = "text/html"
        return super().__init__(data, *args, **kwargs)


class HttpTemplateResponse(Response):
    
    def __init__(self, filepath, *args, **kwargs):
        kwargs["mimetype"] = "text/html"

        with open(filepath) as f:
            fileraw = f.read()
        
        data = str(fileraw)
        return super().__init__(data, *args, **kwargs)
