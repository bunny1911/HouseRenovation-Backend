# coding=utf-8

from logging import getLogger
from logging import StreamHandler, FileHandler

from .config import LOGGING_LEVEL, LOGGING_FILE, LOGGING_PATH, LOGGING_STREAM


logger = getLogger("app")

# Add file handler
LOGGING_PATH.mkdir(parents=True, exist_ok=True)
file_handler = FileHandler(LOGGING_FILE)
file_handler.setLevel(LOGGING_LEVEL)
logger.addHandler(file_handler)

if LOGGING_STREAM:
    # Add stream handler
    stream_handler = StreamHandler()
    stream_handler.setLevel(LOGGING_LEVEL)
    logger.addHandler(stream_handler)
