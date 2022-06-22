import sys
from pathlib import Path


sys.path.insert(0, Path(__file__).resolve().parent.parent.parent.as_posix())  # NOQA

from tutorial.main import app_day03, setup_routes, setup_error_handlers


app = app_day03
setup_routes("tutorial.routes")
setup_error_handlers("tutorial.day03.handlers.error")
