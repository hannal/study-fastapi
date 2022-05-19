import typing as t
import enum

from pydantic import SecretStr

from contrib.conf.base import BaseAppSettings, BaseEnvName
from contrib.types import DatabaseUrlsType


__all__ = [
    "EnvName",
    "environments",
]


@enum.unique
class EnvName(BaseEnvName):
    LOCAL = "local"
    TEST = "test"


@enum.unique
class DatabaseKey(enum.Enum):
    DEFAULT = "default"


class LocalAppSettings(BaseAppSettings):
    database_urls: DatabaseUrlsType = {
        "default": "sqlite:///db.sqlite3",
    }
    default_database = "default"
    secret_key: SecretStr = "secret-key"

    class Config:
        env_file = ".env.local"


class TestAppSettings(BaseAppSettings):
    database_urls: DatabaseUrlsType = {
        "default": "sqlite:///test-db.sqlite3",
    }
    default_database = "default"
    secret_key: SecretStr = "secret-key"

    class Config:
        env_file = ".env.test"


environments: t.Dict[EnvName, t.Type[BaseAppSettings]] = {
    EnvName.LOCAL: LocalAppSettings,
    EnvName.TEST: TestAppSettings,
}
