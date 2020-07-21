# Own
import myapp


def test_helpers_get_something():
    """Does the function retrieve what's expected?"""
    assert myapp.helpers.get_something() == "Hello You!"
