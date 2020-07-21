# Own
import myapp


def test_core_return_code():
    """Does the program quit correctely?"""
    assert myapp.main() == 0
