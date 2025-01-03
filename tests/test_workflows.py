import pytest

from github_actions import dummy_code


def test_dependencies_installed():
    try:
        import flask
        assert flask.__version__
    except ImportError:
        pytest.fail("Flask dependency is missing!")


def test_dummy_code():
    assert dummy_code.make_all_caps("foo") == "FOO"
