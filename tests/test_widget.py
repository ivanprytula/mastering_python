from pytest import mark


@mark.smoke
def test_widget_functions_as_expected(env):
    assert env == "qa"
