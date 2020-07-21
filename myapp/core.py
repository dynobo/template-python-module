"""Main logic of myapp."""

# Standard
import logging
import logging.config

# Extra

# Own
from . import helpers
from . import configs


def main():
    """Start main routine."""
    logging.config.dictConfig(configs.LOGGING)
    logger = logging.getLogger(__name__)
    logger.info("Starting v%s ...", configs.MODULE["version"])
    some_text = helpers.get_something()
    logger.info("Sample output: %s", some_text)
    return 0


if __name__ == "__main__":
    main()
