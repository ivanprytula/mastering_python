"""
The conftest.py/__file__ is used to store fixtures and make them available to any
tests in
their Scope.

[project root directory]
|‐‐ [product code packages]
|-- [test directories]
|   |-- test_*.py
|   `-- *_test.py
|-- README.md
`-- [pytest.ini|tox.ini|setup.cfg]


NB: ⚠ Tests should not share data or state.
NB: ✅ Tests should be modular, deterministic and meaningful

You can think of a test as being broken down into four steps:
- Arrange
- Act
- Assert
- Cleanup

"""
from collections import namedtuple

import requests
from pytest import fixture

from src.demos_examples import Wallet


# Customizing Test Runs with the Command Line and Configuration Files
class Config:
    def __init__(self, env: str) -> None:
        # SUPPORTED_ENVS = ["dev", "qa"]
        # if env.lower() not in SUPPORTED_ENVS:
        #     raise Exception(f"{env} is not supported env...")

        self.base_url = {"dev": "https://mydev-dev.com", "qa": "https://mydev-qa.com"}[
            env
        ]

        self.app_port = {"dev": 8080, "qa": 80}[env]


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        # default="dev"
        help="Envs to run tests against.",
    )


@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@fixture(scope="session")
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture
def user():
    """

    - `@pytest.fixture `- this decorator indicates that this function has a Setup and
    Teardown
    - `def user():` - define the function like normal. `user` will be the name of the
    fixture to be used in tests
    - Everything _before_ the `yield` is executed before each test
    - `yield new_user` - returns new_user and gives control back to the test. The rest
    of the function is not executed yet
    Everything _after_ the `yield` is executed after each test

    """
    # A list of strings for the field names
    User = namedtuple("User", ["name", "age", "salary", "currency"])
    # A string with each field name separated by whitespace
    User1 = namedtuple("User1", "name age salary currency")
    # A string with comma-separated field names
    User2 = namedtuple("User2", "name, age, salary, currency")

    # A generator expression for the field names
    # This last option might look like overkill in this example.
    # However, it’s intended to illustrate the flexibility of the process.
    # UserN = namedtuple("UserN", (field for field in "xyz"))

    new_user = User("Bob", 30, 100_000, "USD")
    new_user1 = User1(name="Bob1", age=40, salary=200_000, currency="CAD")
    new_user2 = User2(
        **{"name": "Bob1", "age": 40, "salary": 200_000, "currency": "CAD"}
    )

    yield new_user
    yield new_user1
    yield new_user2
    del new_user


@fixture(autouse=True)
def disable_network_calls(monkeypatch):
    """Ensures that network calls will be disabled in every test across the suite.
     Any test that executes code calling requests.get() will raise a RuntimeError
    indicating that an unexpected network call would have occurred."""

    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())


@fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")


# Arrange
@fixture
def my_wallet():
    """Returns a Wallet instance with a zero balance"""
    return Wallet()
