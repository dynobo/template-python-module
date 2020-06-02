# Own
from .context import app


def test_helpers_get_something():
    """Does the function retrieve what's expected?"""
    assert app.helpers.get_something() == "Hello You!"
