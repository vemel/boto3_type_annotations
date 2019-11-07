import logging
from typing import Text


def get_logger(name: Text = "builder", verbose: bool = False) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s %(name)s: %(levelname)-8s %(message)s"
        )
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        logger.setLevel(logging.INFO)

    if verbose:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)

    return logger
