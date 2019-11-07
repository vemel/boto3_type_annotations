import logging
from typing import Text


def get_logger(name: Text) -> logging.Logger:
    logger = logging.getLogger(name)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(name)s: %(levelname)-8s %(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)
    return logger
