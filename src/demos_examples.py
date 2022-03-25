from pathlib import Path

import requests


def get_ssh():
    """Simple function to return expanded homedir ssh path."""
    return Path.home() / ".ssh"


def get_json(url):
    """Takes a URL, and returns the JSON."""
    r = requests.get(url)
    return r.json()


class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount("Not enough available to spend {}".format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
