import typing as t
import os
import importlib
from functools import lru_cache

from .base import BaseAppSettings


@lru_cache
def load_settings(
    settings_module_name: t.Optional[str], env_name: t.Optional[str]
) -> BaseAppSettings:
    if not settings_module_name:
        settings_module_name = os.environ.get("APP_SETTINGS_MODULE")
    if not settings_module_name:
        raise ModuleNotFoundError("APP_SETTINGS_MODULE envvar is not set")
    mod = importlib.import_module(settings_module_name)

    if not env_name:
        env_name = os.environ.get("APP_ENV_NAME")
    if not env_name:
        raise ModuleNotFoundError("APP_ENV_NAME envvar is not set")

    env = mod.EnvName.get_member_by_value(env_name)
    settings_class: t.Type[BaseAppSettings] = mod.environments[env]
    return settings_class()
