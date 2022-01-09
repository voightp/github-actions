from datetime import datetime

from src import dummy_code


def test_dependencies_installed():
    import pendulum
    assert isinstance(pendulum.datetime(2021, 5, 1), datetime)


def test_dummy_code():
    assert dummy_code.make_all_caps("foo") == "FOO"
