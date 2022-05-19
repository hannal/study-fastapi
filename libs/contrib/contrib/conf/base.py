import typing as t
import enum
import logging

from pydantic import BaseSettings as _BaseSettings
from pydantic import RedisDsn, SecretStr

from ..types import EnvNameType, DatabaseUrlsType


__all__ = [
    "BaseEnvName",
    "BaseSettings",
    "BaseAppSettings",
]


class BaseSettings(_BaseSettings):
    app_env: EnvNameType = None

    class Config:
        env_file = ".env"


class BaseEnvName(enum.Enum):
    @classmethod
    def get_member_by_value(cls, value) -> "BaseEnvName":
        if isinstance(value, cls):
            return cls.get_member_by_name(value.name)
        for item in cls:
            if item.value == value:
                return item

    @classmethod
    def get_member_by_name(cls, name, silent=True) -> t.Optional["BaseEnvName"]:
        try:
            return cls[name]
        except KeyError:
            if not silent:
                raise
            return


class BaseAppSettings(BaseSettings):
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "FastAPI example application"
    version: str = "0.1.0"

    database_urls: DatabaseUrlsType
    default_database: str

    cache_url: t.Optional[RedisDsn]

    max_connection_count: int = 10
    min_connection_count: int = 10

    secret_key: SecretStr

    api_prefix: str = "/api"

    jwt_token_prefix: str = "Token"

    allowed_hosts: t.List[str] = ["*"]

    logging_level: int = logging.INFO
    loggers: t.Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> t.Dict[str, t.Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
