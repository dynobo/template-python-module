"""Tests for helper functions of myapp."""

# Own
import myapp.helpers


def test_helpers_get_something():
    """Does the function retrieve what's expected?"""
    assert myapp.helpers.get_something() == "Hello You!"
