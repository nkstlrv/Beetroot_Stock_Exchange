from simulator_main import Exchange
import pytest


@pytest.fixture
def exchange_class():
    return Exchange(r"demo_test_data.json")


def test_successful_buy(exchange_class):
    assert exchange_class.portfolio == {"TEST": 1, "MSFT": 2}
    assert exchange_class.buy('aapl', 2) is True
    assert exchange_class.portfolio == {"TEST": 1, "MSFT": 2, "AAPL": 2}
    assert exchange_class.data['balance'] < 1000

    # Teardown
    exchange_class.data = {"portfolio": {"TEST": 1, "MSFT": 2}, "balance": 1000}
    exchange_class.save_data()


def test_buy_non_existing_ticker(exchange_class):
    assert exchange_class.buy('non_existing_ticker', 10) is False
    assert exchange_class.portfolio == {"TEST": 1, "MSFT": 2}
    assert exchange_class.data['balance'] == 1000


def test_not_enough_balance(exchange_class):
    assert exchange_class.buy('aapl', 99999999999) is False
    assert exchange_class.portfolio == {"TEST": 1, "MSFT": 2}
    assert exchange_class.data['balance'] == 1000