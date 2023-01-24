import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def create_logger(name: str, location: str = "", max_bytes: int = 1000000,
                  backup_count: int = 20) -> logging.Logger:
    if not location:
        # default log path: $HOME/logs
        location = '{}/logs'.format(Path.home())

    # try to create dir in case it doesn't exist
    Path(location).mkdir(exist_ok=True)
    logger = logging.getLogger()
    handler = RotatingFileHandler('{}/{}.log'.format(location, name),
                                  maxBytes=max_bytes, backupCount=backup_count)
    log_format = logging.Formatter("%(asctime)s %(name)s %(levelname)s : %(message)s")
    handler.setFormatter(log_format)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
