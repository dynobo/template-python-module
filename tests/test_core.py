# Own
import myapp.core


def test_core_return_code():
    """Does the program quit correctely?"""
    assert myapp.core.main() == 0
