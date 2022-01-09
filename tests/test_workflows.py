from datetime import datetime

from some_package.dummy_code import make_all_caps


def test_dependencies_installed():
    import pendulum
    assert isinstance(pendulum.datetime(2021, 5, 1), datetime)


def test_dummy_code():
    assert make_all_caps("foo") == "FOO"
