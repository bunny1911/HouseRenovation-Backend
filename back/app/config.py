# coding=utf-8

from os import environ
from pathlib import Path
from logging import getLevelName
from dotenv import load_dotenv


def get_var(key: str, missing_ok: bool = False) -> str | None:
    try:
        # Return if exists
        assert missing_ok or (key in environ)
        return environ.get(key)

    except (AssertionError, KeyError):
        # Not found
        raise KeyError(f"Environment variable '{key}' must be specified")


# Database parameters
DB_USERNAME = get_var("DB_USERNAME")
DB_PASSWORD = get_var("DB_PASSWORD")
DB_HOST = get_var("DB_HOST")
DB_NAME = get_var("DB_NAME")

# Logging
LOGGING_LEVEL = getLevelName(get_var("LOGGING_LEVEL", missing_ok=True) or "WARNING")
LOGGING_PATH = Path(get_var("LOGGING_PATH", missing_ok=True) or "logs")
LOGGING_FILE = LOGGING_PATH / (get_var("LOGGING_FILE", missing_ok=True) or "app.log")
LOGGING_STREAM = int(get_var("LOGGING_STREAM", missing_ok=True) or 0)

# Sentry logging
SENTRY_DSN = get_var("SENTRY_DSN", missing_ok=True)
SENTRY_TRACES_SAMPLE_RATE = 1.0
