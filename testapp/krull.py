import sys, os

pythonpath = sys.path
krullpath = os.environ.get("krullpath", None)

in_path = False
for path in pythonpath:
    if path == krullpath:
        in_path = True

if not in_path:
    sys.path.append(krullpath)

from server import run_krull
from core import build_app

app = build_app()

if __name__ == '__main__': 
    run_krull(app)

