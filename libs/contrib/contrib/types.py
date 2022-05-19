import typing as t
import enum

from pydantic import FileUrl
from pydantic import PostgresDsn


__all__ = [
    "SqlLiteDsn",
    "EnvNameType",
    "DatabaseUrlsType",
]


class SqlLiteDsn(FileUrl):
    allowed_schemes = {"sqlite"}
    host_required = False


EnvNameType: t.TypeAlias = enum.Enum

DatabaseUrlsType = t.Dict[str, t.Union[PostgresDsn, SqlLiteDsn]]
