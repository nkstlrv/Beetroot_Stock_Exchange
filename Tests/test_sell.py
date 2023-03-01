from simulator_main import Exchange
import pytest


@pytest.fixture
def exchange_class():
    return Exchange(r"demo_test_data.json")


def test_successful_sell(exchange_class):
    assert exchange_class.data == {"portfolio": {"TEST": 1, "MSFT": 2}, "balance": 1000}
    assert exchange_class.sell('msft', 1) is True
    assert exchange_class.portfolio == {"TEST": 1, "MSFT": 1}
    assert exchange_class.data['balance'] > 1000

    # Teardown
    exchange_class.data = {"portfolio": {"TEST": 1, "MSFT": 2}, "balance": 1000}
    exchange_class.save_data()


def test_buy_non_existing_ticker(exchange_class):
    assert exchange_class.sell('non_existing_ticker', 1) is False
    assert exchange_class.data == {"portfolio": {"TEST": 1, "MSFT": 2}, "balance": 1000}


def test_sell_but_not_enough_tickers(exchange_class):
    assert exchange_class.sell('msft', 999999999999) is False
    assert exchange_class.data == {"portfolio": {"TEST": 1, "MSFT": 2}, "balance": 1000}