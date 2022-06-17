import sys
from pathlib import Path


sys.path.insert(0, Path(__file__).resolve().parent.parent.parent.as_posix())  # NOQA

from tutorial.main import app_day03, setup_routes


app = app_day03
setup_routes("tutorial.routes")
