"""Provides unspecific helper functions."""

# Standard
import logging


def get_something():
    """Dummy function."""
    logger = logging.getLogger(__name__)
    logger.info("Logging from subroutine")
    return "Hello You!"
