import typing as t
import sys
import logging

from loguru import logger


HandlerType = tuple[t.Callable, t.Union[dict, None]] | t.Callable | t.Any

HandlerParamType = list[HandlerType]


def configure_logging(
    loggers: t.Tuple[str, str],
    handlers: HandlerParamType,
    logging_level: int,
) -> None:
    logging.getLogger().handlers = [
        _init_handler(_handler, False) for _handler in handlers
    ]
    for logger_name in loggers:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [_init_handler(_handler) for _handler in handlers]

    logger.configure(handlers=[{"sink": sys.stderr, "level": logging_level}])


def _init_handler(handler: HandlerType, with_kwargs=True):
    if isinstance(handler, (tuple, list)):
        _handler, kwargs, *__ = handler
        return (
            _handler(**kwargs)
            if isinstance(kwargs, dict) and with_kwargs
            else _handler()
        )
    elif callable(handler):
        return handler()
    else:
        return handler
