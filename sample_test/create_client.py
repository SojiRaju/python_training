# test_client.py

import pytest
from client import Client


@pytest.fixture
def client():
    return Client("John Daniel")


def test_client_deposit(client):
    client.deposit(100)
    assert client.get_balance() == 100


def test_client_withdraw_sufficient_balance(client):
    client.deposit(100)
    client.withdraw(50)
    assert client.get_balance() == 50


def test_client_withdraw_insufficient_balance(client):
    with pytest.raises(ValueError):
        client.withdraw(50)


def test_client_initial_balance_zero(client):
    assert client.get_balance() == 0
