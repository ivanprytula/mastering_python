# contents of test_app.py, a simple test for our API retrieval
# import requests for the purposes of monkeypatching
from pathlib import Path

import requests
from pytest import fixture, mark

# our app.py that includes the get_json() function
# this is the previous code block example
from src.demos_examples import get_json, get_ssh


# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


# monkeypatched requests.get moved to a fixture
@fixture
def mock_response(monkeypatch):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


# def test_get_json(monkeypatch):
#     # Any arguments may be passed and mock_get() will always return our
#     # mocked object, which only has the .json() method.
#     def mock_get(*args, **kwargs):
#         return MockResponse()
#
#     # apply the monkeypatch for requests.get to mock_get
#     monkeypatch.setattr(requests, "get", mock_get)
#
#     # demo_app.get_json, which contains requests.get, uses the monkeypatch
#     result = src.demo_app.get_json("https://fakeurl")
#     assert result["mock_key"] == "mock_response"


# notice our test uses the custom fixture instead of monkeypatch directly
def test_get_json(mock_response):
    result = get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"


@mark.parametrize("earned,spent,expected", [(30, 10, 20), (20, 2, 18)])
def test_transactions(my_wallet, earned, spent, expected):
    # Act
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)

    # Assert
    assert my_wallet.balance == expected


def test_get_ssh(monkeypatch):
    # mocked return function to replace Path.home
    # always return '/abc'
    def mock_return():
        return Path("/abc")

    # Application of the monkeypatch to replace Path.home
    # with the behavior of mock_return defined above.
    monkeypatch.setattr(Path, "home", mock_return)

    # Calling get_ssh() will use mock_return in place of Path.home
    # for this test with the monkeypatch.
    x = get_ssh()
    assert x == Path("/abc/.ssh")
