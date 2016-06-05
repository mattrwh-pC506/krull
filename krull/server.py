from http.server import HTTPServer, BaseHTTPRequestHandler


def run_server(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 6174)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
