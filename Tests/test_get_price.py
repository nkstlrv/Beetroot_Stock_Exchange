from simulator_main import Exchange
import pytest


# This fixture creates an instance of the Exchange class
@pytest.fixture
def create_exchange_class():
    return Exchange(r"Data\my_data.json")


# Testing get_price method
def test_get_price_of_real_tickers(create_exchange_class):

    assert create_exchange_class.get_price("GOOGL")[:22] == "Market price for GOOGL"
    assert (create_exchange_class.get_price("GOOGL")[-1]).isdigit() is True

    assert create_exchange_class.get_price("MSFT")[:21] == "Market price for MSFT"
    assert (create_exchange_class.get_price("MSFT")[-1]).isdigit() is True

    assert create_exchange_class.get_price("AAPL")[:21] == "Market price for AAPL"
    assert (create_exchange_class.get_price("AAPL")[-1]).isdigit() is True


# Testing raising error if ticker doesn't exist
def test_get_price_of_nonexisting_ticker(create_exchange_class):

    with pytest.raises(IndexError) as ex_info:

        create_exchange_class.get_price("Non Existing Ticker")
        create_exchange_class.get_price("Another non Existing Ticker")
        create_exchange_class.get_price("")
        create_exchange_class.get_price("1234")

    assert "single positional indexer is out-of-bounds" == str(ex_info.value)

