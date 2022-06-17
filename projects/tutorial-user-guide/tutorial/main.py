import sys
from pathlib import Path
from importlib import import_module

from fastapi import FastAPI


__all__ = [
    "create_app",
    "setup_routes",
    "app",
    "app_day03",
]

sys.path.insert(0, Path(__file__).resolve().parent.parent.as_posix())


def create_app(*args, **kwargs):
    application = FastAPI(*args, **kwargs)

    return application


def setup_routes(routes_namespace: str):
    import_module(routes_namespace)


app = create_app()

app_day03 = create_app(
    debug=True,
    title="FastAPI Study - day03",
)
