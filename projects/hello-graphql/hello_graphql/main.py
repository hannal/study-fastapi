import os

from loguru import logger
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from contrib.conf import load_settings
from contrib.conf.base import BaseAppSettings
from contrib.logging.boot import configure_logging
from contrib.logging.handlers import InterceptHandler

from handlers import errors as error_handlers
from .routes import router


__all__ = [
    "create_app",
    "app",
]


if not os.environ.get("APP_SETTINGS_MODULE"):
    os.environ.setdefault("APP_SETTINGS_MODULE", "hello_graphql.settings")

if not os.environ.get("APP_ENV_NAME"):
    os.environ.setdefault("APP_ENV_NAME", "local")


def create_app():
    settings = load_settings(
        os.environ.get("APP_SETTINGS_MODULE"),
        os.environ.get("APP_ENV_NAME"),
    )

    application = FastAPI(**settings.fastapi_kwargs, settings=settings)

    setup_logging(settings)

    if settings.debug:
        logger.info("Running in development mode")
        setup_cors(application, settings)

    for _path, _name, _options in [
        ["_assets", "assets", {"html": True}],
    ]:
        setup_static(application, _path, _name, _options)

    application.include_router(router)
    setup_exception_handlers(application)

    return application


def setup_cors(application: FastAPI, settings: BaseAppSettings):
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    logger.info("CORS is enabled")


def setup_logging(settings: BaseAppSettings):
    configure_logging(
        settings.loggers,
        [
            [InterceptHandler, {"level": settings.logging_level}],
        ],
        settings.logging_level,
    )
    logger.info("Logging is configured")


def setup_exception_handlers(application: FastAPI):
    application.add_exception_handler(HTTPException, error_handlers.http_error_handler)
    application.add_exception_handler(
        RequestValidationError, error_handlers.http422_error_handler
    )
    logger.info("Exception handlers are initialized")


def setup_static(application: FastAPI, path: str, name: str, options: dict | None):
    if os.path.isdir(path):
        application.mount(
            f"/{path[1:]}",
            StaticFiles(directory=path, **(options or {})),
            name=name,
        )
        logger.info(f"[{name}] assets are mounted")


app = create_app()
