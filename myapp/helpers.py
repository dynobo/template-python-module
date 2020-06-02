# Standard
import logging


def get_something():
    logger = logging.getLogger(__name__)
    logger.info("Logging from subroutine")
    return "Hello You!"
