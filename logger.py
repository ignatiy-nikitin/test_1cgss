import sys

from loguru import logger

from settings import LOGGING_LEVEL, LOGGING_FILE_PATH


def init_logger():
    logger.add(LOGGING_FILE_PATH, format='{time} {level} - {name}:{function}:{line} -- {message}', level=LOGGING_LEVEL)
    logger.configure(handlers=[{'sink': sys.stderr, 'level': LOGGING_LEVEL}])
