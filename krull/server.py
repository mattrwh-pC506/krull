from core import spawn_krull
from werkzeug.serving import run_simple


def run_krull():
    krull = spawn_krull()
    return run_simple('127.0.0.1', 5000, krull)


if __name__ == '__main__':
    run_krull()
