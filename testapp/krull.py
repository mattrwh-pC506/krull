import sys, os

pythonpath = sys.path
krullpath = os.environ.get("krullpath", None)
print (krullpath, pythonpath)

in_path = False
for path in pythonpath:
    if path == krullpath:
        in_path = True

if not in_path:
    sys.path.append(krullpath)

from server import run_krull
from core import build_app

APP_LABEL = "Test App"


app = build_app({
    "app_label": APP_LABEL
    })

if __name__ == '__main__': 
    run_krull(app)

