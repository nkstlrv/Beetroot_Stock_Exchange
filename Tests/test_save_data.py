from simulator_main import Exchange
import pytest


@pytest.fixture
def exchange_class():
    return Exchange(r"demo_test_data.json")


def test_save_data(exchange_class):
    assert exchange_class.portfolio == {"TEST": 1, "MSFT": 2}
    exchange_class.data['portfolio'] = {"a": None}
    exchange_class.save_data()
    assert exchange_class.data['portfolio'] == {"a": None}
    assert exchange_class.data == {"portfolio": {"a": None}, "balance": 1000}

    # Teardown
    exchange_class.data['portfolio'] = {"TEST": 1, "MSFT": 2}
    exchange_class.save_data()

