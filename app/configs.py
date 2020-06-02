MODULE = {
    "name": "app",
    "author": "dynobo",
    "email": "dynobo@mailbox.org",
    "repo": "https://github.com/dynobo/app",
    "version": "0.1.0",
}

LOGGING = {
    "loggers": {"app": {"level": "INFO", "propagate": False, "handlers": ["console"]}},
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
            "format": "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",  # noqa: longline okay
        }
    },
}
