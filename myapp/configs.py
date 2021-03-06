"""Provides all configurations in one place."""

# pylint: disable=C0301 # line-to-long

MODULE = {
    "name": "myapp",
    "author": "dynobo",
    "email": "dynobo@mailbox.org",
    "repo": "https://github.com/dynobo/myapp",
    "version": "0.1.0",
}

LOGGING = {
    "loggers": {
        "myapp": {"level": "INFO", "propagate": False, "handlers": ["console"]}
    },
    "version": 1,
    "disable_existing_loggers": True,
    "handlers": {
        "console": {
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "DEBUG",
        },
        "file": {
            "formatter": "standard",
            "backupCount": 10,
            "level": "WARNING",
            "encoding": "utf8",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 10485760,
            "filename": "/tmp/warnings.log",
        },
    },
    "root": {"level": "ERROR", "handlers": ["console", "file"]},
    "formatters": {
        "standard": {
            "datefmt": "%H:%M:%S",
            "format": "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",  # noqa
        }
    },
}
