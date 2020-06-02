# Own
from .context import app


def test_core_return_code():
    """Does the program quit correctely?"""
    assert app.main() == 0
