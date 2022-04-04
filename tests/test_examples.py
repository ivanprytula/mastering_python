from pytest import mark


def test_always_passes():
    assert True


@mark.skip
def test_always_fails():
    assert False


def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


@mark.skip
def test_needsfiles(tmp_path):
    """We can request arbitrary resources, like a unique temporary directory."""
    print(tmp_path)
    assert 0


@mark.skip
@mark.smoke
def test_widget_functions_as_expected(env):
    assert env == "qa"


@mark.skip
class TestClass:
    """
    Grouping tests in classes can be beneficial for the following reasons:
    - Test organization
    - Sharing fixtures for tests only in that particular class
    - Applying marks at the class level and having them implicitly apply to all tests

    Something to be aware of when grouping tests inside classes is that each test
    has a unique instance of the class. Having each test share the same class instance
    would be very detrimental to test isolation and would promote poor test practices.
    """

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


def is_palindrome(palindrome: str):
    return True


@mark.skip
@mark.parametrize("non_palindrome", ["abc", "abab"])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)


# Combines above two tests into one:
@mark.skip
@mark.parametrize(
    "maybe_palindrome, expected_result",
    [
        ("", True),
        ("a", True),
        ("Bob", True),
        ("Never odd or even", True),
        ("Do geese see God?", True),
        ("abc", False),
        ("abab", False),
    ],
)
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result
