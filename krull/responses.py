import json

from werkzeug.wrappers import Response


class JsonResponse(Response):
    
    def __init__(self, data, *args, **kwargs):
        json_data = json.dumps(data)
        return super().__init__(json_data, *args, **kwargs)
