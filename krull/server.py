from werkzeug.serving import run_simple


def run_krull(app):
    return run_simple('127.0.0.1', 5000, app)

