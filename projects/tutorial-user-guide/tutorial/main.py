from fastapi import FastAPI


__all__ = [
    "create_app",
    "app",
]


def create_app():
    application = FastAPI()
    return application


app = create_app()
