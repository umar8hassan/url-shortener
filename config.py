"""Setting for URL Shortener App."""

import os
from typing import Any, Type, TypeVar

from dotenv import load_dotenv

from app.exceptions import ConfigError

load_dotenv()

CastType = TypeVar("CastType", str, int, bool)


def get_env(
    var: str,
    required: bool = False,
    cast: Type[CastType] = str,
    default: Any | None = None,
) -> Any:
    """Get env variables with default or non-empty values."""
    value = os.getenv(var) or cast()

    if not isinstance(value, cast):
        value = cast(value)

    if not value and default is not None:
        value = default

    if required and value is None:
        raise ConfigError(var)

    return value


class Config:
    """Config Class for the App."""

    LOG_LEVEL = get_env("LOG_LEVEL", default="INFO")
    DEBUG_MODE = get_env("DEBUG_MODE", cast=bool)
    SQLALCHEMY_DATABASE_URI = get_env("SQLALCHEMY_DATABASE_URI", required=True)
    SQLALCHEMY_TRACK_MODIFICATIONS = get_env(
        "SQLALCHEMY_TRACK_MODIFICATIONS", cast=bool
    )
    SECRET_KEY = get_env("SECRET_KEY", required=True)
