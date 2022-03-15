import importlib


def get_zen():
    importlib.import_module("this")


if __name__ == "__main__":
    get_zen()
